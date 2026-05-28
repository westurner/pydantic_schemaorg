"""
test_main.py
"""

import argparse
import os
import pytest
import sys
from src import main


def test_generate_schemaorg_models(monkeypatch, tmp_path):
    # Patch network call to avoid real HTTP request
    # class DummyResponse:
    #     def read(self):
    #         # Minimal valid schema.org JSON-LD structure
    #         return b'{"@graph": [{"@id": "schema:TestClass", "@type": "schema:Thing", "rdfs:comment": "A test class."}]}'
    # monkeypatch.setattr(main.request, "urlopen", lambda url: DummyResponse())
    testpath = tmp_path / "output"
    testpath.mkdir()

    classes = main.generate_schemaorg_models(testpath, schemaorg_url="dummy_url")
    assert "CreativeWork" in classes
    assert "Zoo" in classes

    # Check that output files are created
    out_dir = testpath
    generated_module_file_names = os.listdir(out_dir)
    assert "CreativeWork.py" in generated_module_file_names
    assert "Zoo.py" in generated_module_file_names


def test_generate_schemaorg_models_dummy(monkeypatch, tmp_path):
    # Patch network call to avoid real HTTP request
    class DummyResponse:
        def read(self):
            # Minimal valid schema.org JSON-LD structure
            return b'{"@graph": [{"@id": "schema:TestClass", "@type": "schema:Thing", "rdfs:comment": "A test class."}]}'

    monkeypatch.setattr(main.request, "urlopen", lambda url: DummyResponse())
    monkeypatch.setattr(
        main, "get_from_disk_or_http", lambda *args: DummyResponse.read(None)
    )

    testpath = tmp_path / "output"
    testpath.mkdir()

    classes = main.generate_schemaorg_models(testpath, schemaorg_url="dummy_url")
    assert "TestClass" in classes
    # Check that output files are created

    out_dir = testpath
    generated_module_file_names = os.listdir(out_dir)
    assert "TestClass.py" in generated_module_file_names


def test_build_parser_structure():
    """Test that build_parser returns an ArgumentParser with expected subcommands."""
    parser = main.build_parser()
    assert isinstance(parser, argparse.ArgumentParser)
    # Check top-level commands
    subparsers_action = next(
        (a for a in parser._actions if isinstance(a, argparse._SubParsersAction)), None
    )
    assert subparsers_action is not None
    commands = subparsers_action.choices.keys()
    assert "build" in commands
    assert "report" in commands
    assert "test" in commands


def test_main_help(monkeypatch, capsys):
    """Test main.main prints help and exits when --help is passed."""
    monkeypatch.setattr(sys, "argv", ["main.py", "--help"])
    with pytest.raises(SystemExit):
        main.main(argv=sys.argv)
    captured = capsys.readouterr()
    assert "Build pydantic_schemaorg Python classes" in captured.out
    assert "build" in captured.out
    assert "report" in captured.out
    assert "test" in captured.out


def test_main_build_base(monkeypatch, tmp_path):
    """Test main.main with build base command generates SchemaOrgBase.py."""
    # Patch network and file operations
    monkeypatch.setattr(main, "init_package", lambda: None)
    monkeypatch.setattr(
        main,
        "write_base_class",
        lambda: tmp_path.joinpath("SchemaOrgBase.py").write_text("# base class\n"),
    )
    monkeypatch.setattr(main, "generate_schemaorg_models", lambda *a, **kw: [])
    monkeypatch.setattr(
        sys, "argv", ["main.py", "build", "base", "--target", str(tmp_path)]
    )
    main.main(argv=sys.argv)
    assert tmp_path.joinpath("SchemaOrgBase.py").exists()
    assert "base class" in tmp_path.joinpath("SchemaOrgBase.py").read_text()


def test_main_build_all(monkeypatch, tmp_path):
    """Test main.main with build all command generates models and base class."""
    monkeypatch.setattr(main, "init_package", lambda: None)
    monkeypatch.setattr(
        main,
        "write_base_class",
        lambda: tmp_path.joinpath("SchemaOrgBase.py").write_text("# base class\n"),
    )
    monkeypatch.setattr(
        main, "generate_schemaorg_models", lambda *a, **kw: ["TestClass"]
    )
    monkeypatch.setattr(
        sys, "argv", ["main.py", "build", "all", "--target", str(tmp_path)]
    )
    main.main(argv=sys.argv)
    assert tmp_path.joinpath("SchemaOrgBase.py").exists()
    assert "base class" in tmp_path.joinpath("SchemaOrgBase.py").read_text()


def test_main_build_models(monkeypatch, tmp_path):
    """Test main.main with build models command generates models only."""
    monkeypatch.setattr(main, "init_package", lambda: None)
    monkeypatch.setattr(main, "write_base_class", lambda: None)
    monkeypatch.setattr(
        main, "generate_schemaorg_models", lambda *a, **kw: ["TestClass"]
    )
    monkeypatch.setattr(
        sys, "argv", ["main.py", "build", "models", "--target", str(tmp_path)]
    )
    main.main(argv=sys.argv)
    # Should call generate_schemaorg_models, but not write_base_class
    # No file assertion since write_base_class is patched to None


def test_main_report_counts(monkeypatch, capsys):
    """Test main.main with report counts prints class/property counts."""
    dummy_jsonld = {
        "@graph": [
            {"@id": "schema:TestClass", "@type": "schema:Thing"},
            {"@id": "schema:TestProp", "@type": "rdf:Property"},
        ]
    }
    monkeypatch.setattr(main, "read_schemaorg_jsonld", lambda *a, **kw: dummy_jsonld)
    monkeypatch.setattr(sys, "argv", ["main.py", "report", "counts"])
    main.main(argv=sys.argv)
    captured = capsys.readouterr()
    assert "RDFS Classes: 1" in captured.out
    assert "RDFS Properties: 1" in captured.out


# TODO: coverage on this
# def test_main_test_command(monkeypatch):
#     """Test main.main with test command runs pytest."""
#     called = {}
#     def fake_run(cmd):
#         called['ran'] = cmd
#         return 0
#     monkeypatch.setattr(sys, "argv", ["main.py", "test"])
#     monkeypatch.setattr("subprocess.run", fake_run)
#     main.main(argv=sys.argv)
#     assert called['ran'] == ["pytest", "-x"]
