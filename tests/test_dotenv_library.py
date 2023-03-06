import os
import pytest
from RobotDotenv import DotenvLibrary


@pytest.fixture
def lib() -> DotenvLibrary:
    yield DotenvLibrary()


@pytest.fixture(autouse=True)
def change_test_dir(request, monkeypatch):
    monkeypatch.chdir(request.fspath.dirname)


def test_load(lib):
    assert os.environ.get("FIRST") is None
    lib.load_dotenv(".env")
    assert os.environ.get("FIRST") == "1"


def test_load_multiple_vars(lib):
    assert os.environ.get("SECOND") is None
    assert os.environ.get("THIRD") is None
    lib.load_dotenv(".env.1")
    assert os.environ.get("SECOND") == "2"
    assert os.environ.get("THIRD") == "3"
