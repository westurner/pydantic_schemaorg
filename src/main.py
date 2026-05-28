"""
main.py
"""
import datetime
import argparse
import json
import logging
import os
import shutil
import sys

from typing import Optional, Union

from http.client import HTTPResponse
from pathlib import Path
from urllib import request

from src.constants import data_type_map, PACKAGE_NAME, data_type_specificity
from src.jinja import jinja_env
from src.schema_org import SchemaOrg

THIS_PATH: Path = Path(__file__).parent
CACHE_PATH: Union[str, Path] = THIS_PATH / 'schema'
SCHEMAORG_JSONLD_URL: str = "https://schema.org/version/latest/schemaorg-current-https.jsonld"

PARSERS: dict = None


logging.basicConfig(
    format='%(levelname)-6s\t%(name-7)s\t%(message)s'
)
log = logging.getLogger('main')


def get_from_disk_or_http(url: str, filename: Optional[str]=None, cache_dir: Optional[Path]=CACHE_PATH, text: bool=False) -> Union[str, bytes]:
    """
    Download a file from a URL or read it from disk cache. Optionally decode as text.
    Args:
        url: The URL to fetch.
        filename: Optional filename for cache.
        cache_dir: Directory to cache file.
        text: If True, decode as UTF-8 text.
    Returns:
        File contents as bytes or str.
    """

    log.debug(f"get_from_disk_or_http called with url={url}, filename={filename}, cache_dir={cache_dir}, text={text}")
    if url is None:
        log.error("url must not be None")
        raise ValueError("url must not be None")
    if filename is None:
        filename = os.path.basename(url)
        log.debug(f"filename not provided. defaulting to basename(url): {filename}")

    data = None

    if cache_dir is not None:
        cache_dir.mkdir(mode=551, parents=True, exist_ok=True)
        local_file = cache_dir / filename
        log.debug(f"Checking for cached file at {local_file}")
        if local_file.exists():
            log.info(f"Reading from cache: {local_file}")
            if text:
                log.debug("Reading cached data as UTF-8 text")
                with open(local_file, "r", encoding="utf-8", newline="") as f:
                    return f.read()
            else:
                with open(local_file, "rb") as f:
                    data = f.read()
                return data

    log.info(f"Fetching from URL: {url}")
    response: HTTPResponse = request.urlopen(url)
    data = response.read()
    if text:
        encoding = response.headers.get_content_charset() or "utf-8"
        log.debug(f"Decoding fetched data using encoding={encoding}")
        data_to_return = data.decode(encoding)
    else:
        data_to_return = data

    # Optionally cache to disk
    if cache_dir is not None:
        try:
            log.debug(f"Writing fetched data to cache: {local_file}")
            with open(local_file, "wb") as f:
                if text:
                    f.write(data_to_return.encode("utf-8"))
                else:
                    f.write(data_to_return)
            log.info(f"Cached file written: {local_file}")
        except Exception as e:
            log.error(f"Writing to {local_file!r} failed:")
            log.exception(e)
            pass

    return data_to_return


def write_base_class(target_dir: Union[str, Path]=PACKAGE_NAME) -> None:
    """
    Write the SchemaOrgBase.py file from the template.
    """
    target_path = Path(target_dir)
    target_path.mkdir(parents=True, exist_ok=True)
    with open(target_path / "SchemaOrgBase.py", "w") as model_file:
        with open(
                THIS_PATH / "templates/schema_org_base.py.tpl"
        ) as template_file:
            template = jinja_env.from_string(template_file.read())
            template_args = dict(
                schemaorg_version=os.getenv("SCHEMAORG_VERSION"),
                commit=os.getenv("COMMIT"),
                timestamp=datetime.datetime.now(),
            )
        template.stream(**template_args).dump(model_file)


def copy_utils(target_dir: Union[str, Path]=PACKAGE_NAME) -> None:
    """
    Copy ISO8601 utility files to the package directory.
    """
    target_path = Path(target_dir)
    os.makedirs(target_path / 'ISO8601', exist_ok=True)
    for file in os.listdir(f'{THIS_PATH}/ISO8601'):
        if file.endswith('.py'):
            shutil.copy(f'{THIS_PATH}/ISO8601/{file}', target_path / 'ISO8601')


def init_package(target_dir: Union[str, Path]=PACKAGE_NAME) -> None:
    """
    Remove and recreate the package directory, copying utilities.
    """
    target_path = Path(target_dir)
    shutil.rmtree(target_path, ignore_errors=True)
    os.makedirs(target_path, exist_ok=True)
    copy_utils(target_path)


def read_schemaorg_jsonld(
        schemaorg_url: str=SCHEMAORG_JSONLD_URL,
        schema_filename: Optional[str]=None) -> dict:
    """
    Download and parse the schema.org JSON-LD file.
    Args:
        schemaorg_url: URL to schema.org JSON-LD.
        schema_filename: Optional filename for cache.
    Returns:
        Parsed JSON as dict.
    """
    raw_jsonld = get_from_disk_or_http(schemaorg_url, schema_filename)
    schema_data = json.loads(raw_jsonld.decode("utf-8"))
    return schema_data


def generate_schemaorg_models(
        target_dir: Optional[Union[str,Path]],
        schemaorg_url: str=SCHEMAORG_JSONLD_URL,
        schema_filename: Optional[str]=None) -> list[str]:
    """
    Generate all schema.org models and base class files.
    Args:
        target_dir: Output directory for models.
        schemaorg_url: URL to schema.org JSON-LD.
        schema_filename: Optional filename for cache.
    Returns:
        List of generated class names.
    """
    if not target_dir:
        raise ValueError("target_dir must not be None")
    if schema_filename is None:
        schema_filename = Path(SCHEMAORG_JSONLD_URL).name

    target_path = Path(target_dir)
    init_package(target_path)

    write_base_class(target_path)

    schema_data = read_schemaorg_jsonld(schemaorg_url, schema_filename)
    schema_data = {node["@id"]: node for node in schema_data["@graph"]}

    schema_org_api = SchemaOrg(schema_data, data_type_map, data_type_specificity)
    schema_org_class_names = sorted(schema_org_api.get_all_classes())

    for class_ in schema_org_class_names:
        schema_org_pydantic_class = schema_org_api.load_type(class_)
        log.debug(f"Loading class: {class_!r}")

    # TODO: is this second pass necessary?
    for class_ in schema_org_class_names:
        schema_org_pydantic_class = schema_org_api.load_type(class_)
        output = schema_org_api.write_type(schema_org_pydantic_class, target_dir)
        log.debug(f"Wrote: {output['name']} to {output['path']}")

    schema_org_api.write_init()

    return schema_org_class_names


def build_parser() -> argparse.ArgumentParser:
    """
    Build and return the CLI argument parser for all commands.
    Returns:
        Configured ArgumentParser instance.
    """
    parser = argparse.ArgumentParser(description="Build pydantic_schemaorg Python classes", add_help=True)
    #parser.add_argument('-H', '--help-all', dest="help_all", action='store_true', help="show help messages for all commands and exit")

    subparsers = parser.add_subparsers(dest="command", required=False)

    build_desc = "Build pydantic_schemaorg/*.py models"
    build_parser = subparsers.add_parser("build", help=build_desc, description=build_desc, add_help=True)
    build_subparsers = build_parser.add_subparsers(dest="build_command")

    build_all_desc = "Build all source files: base, models"
    build_all_parser = build_subparsers.add_parser("all", help=build_all_desc, description=build_all_desc, add_help=True)
    build_all_parser.add_argument("--target", type=str, default=PACKAGE_NAME, help="Target directory for base class")
    build_all_parser.add_argument("--schema-url", dest="schema_url", type=str, default=SCHEMAORG_JSONLD_URL, help="Schema.org JSON-LD URL")

    build_base_desc = "Build only SchemaOrgBase.py"
    build_base_parser = build_subparsers.add_parser("base", help=build_base_desc, description=build_base_desc, add_help=True)
    build_base_parser.add_argument("--target", type=str, default=PACKAGE_NAME, help="Target directory for base class")

    build_models_desc = "Build all schema.org models"
    build_models_parser = build_subparsers.add_parser("models", help=build_models_desc, description=build_models_desc, add_help=True)
    build_models_parser.add_argument("--target", type=str, default=PACKAGE_NAME, help="Target directory for buildd models")
    build_models_parser.add_argument("--schema-url", dest='schema_url', type=str, default=SCHEMAORG_JSONLD_URL, help="Schema.org JSON-LD URL")


    report_desc = "Build and display reports"
    report_parser = subparsers.add_parser("report", help=report_desc, description=report_desc, add_help=True)
    report_subparsers = report_parser.add_subparsers(dest="report_command")

    report_count_desc = "Show schema.org class/property counts"
    report_count = report_subparsers.add_parser("counts", help=report_count_desc, description=report_count_desc, add_help=True)
    report_count.add_argument("--schema-url", type=str, default=SCHEMAORG_JSONLD_URL, help="Schema.org JSON-LD URL")

    test_parser = subparsers.add_parser("test", help="Run tests using pytest")

    parsers = ((key, dict(key=key, cls=parser, helptext=parser.format_help()[7:]))
                for key, parser in locals().items()
                  if hasattr(parser, 'format_help'))

    next(parsers)  # remove the first element (`parser`)
    global PARSERS 
    PARSERS = dict(parsers)

    parser.formatter_class = formatter_class=argparse.RawDescriptionHelpFormatter
    parser.epilog = '______\n\n' + '__\n\n'.join(v['helptext'] for v in PARSERS.values()) + '______'

    return parser


def main(argv: Optional[list[str]]=[__file__]) -> int:
    """
    Main entry point for pydantic_schemaorg CLI
    """
    parser: argparse.ArgumentParser = build_parser()
    if argv is None:
        argv = sys.argv
    log.debug(('argv', argv))

    args = parser.parse_args(args=argv[1:])
    log.debug(('args', args))

    if not argv[1:] or getattr(args, 'help', False):
        parser.print_help()
        parser.exit(0)

    if '--test' in argv:
        argposindex = argv.index('--test')
        test_args = argv[argposindex+1:]
        argv = argv[:argposindex+1]

    if args.command == "build":
        # Default to 'all' if no subcommand is provided
        generate_cmd = getattr(args, 'build_command', None)

        if generate_cmd is None:
            PARSERS['build_parser']['cls'].print_help()
            return 0

        if generate_cmd == "models" or generate_cmd == "all":
            # Use args from 'all' parser if available, else fallback to defaults
            target = getattr(args, 'target', PACKAGE_NAME)
            schema_url = getattr(args, 'schema_url', SCHEMAORG_JSONLD_URL)
            targetPath = Path(target)
            generate_schemaorg_models(targetPath, schemaorg_url=schema_url)

        if generate_cmd == "base" or generate_cmd == "all":
            target = getattr(args, 'target', PACKAGE_NAME)
            targetPath = Path(target)
            write_base_class(targetPath)
            log.info(f"SchemaOrgBase.py generated at {targetPath}/SchemaOrgBase.py")

    elif args.command == "test":
        import subprocess
        subprocess.run(["pytest", "-x"])

    elif args.command == "report":
        report_cmd = getattr(args, 'report_command', None)
        if report_cmd is None:
            PARSERS['report_parser']['cls'].print_help()
            return 0

        if report_cmd == "all" or report_cmd == "counts":
            schema_url = getattr(args, 'schema_url', SCHEMAORG_JSONLD_URL)
            schema_data = read_schemaorg_jsonld(schema_url)

            # Support both list and dict formats
            if isinstance(schema_data, list):
                nodes = [node for node in schema_data if isinstance(node, dict)]
            elif isinstance(schema_data, dict) and "@graph" in schema_data:
                nodes = [node for node in schema_data["@graph"] if isinstance(node, dict)]
            else:
                nodes = [node for node in schema_data.values() if isinstance(node, dict)]

            class_count = sum(1 for v in nodes if v.get("@type") != "rdf:Property")
            property_count = sum(1 for v in nodes if v.get("@type") == "rdf:Property")

            print(f"RDFS Classes: {class_count}")
            print(f"RDFS Properties: {property_count}")

        else:
            parser.error("report command not recognized")

    # parser.exit(0)
    # sys.exit(0)
    return 0
    


if __name__ == "__main__":
    main(argv=sys.argv)
