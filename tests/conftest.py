"""Fixtures used in all tests."""

from pathlib import Path

import pytest
from _pytest.fixtures import FixtureRequest


collect_ignore: list[str] = ["data", "conf"]
pytest_plugins: list[str] = ["pytester"]


@pytest.fixture(scope="session")
def repository_root(request: FixtureRequest, tests_folder: Path) -> Path:
    return getattr(request, "param", tests_folder.parent)


@pytest.fixture(scope="session")
def tests_folder(request: FixtureRequest) -> Path:
    return getattr(request, "param", Path(__file__).parent)


@pytest.fixture(scope="session")
def unit_tests_folder(request: FixtureRequest, tests_folder: Path) -> Path:
    return getattr(request, "param", tests_folder / "unit_tests")


@pytest.fixture(scope="session")
def integration_tests_folder(request: FixtureRequest, tests_folder: Path) -> Path:
    return getattr(request, "param", tests_folder / "integration_tests")


@pytest.fixture(scope="session")
def acceptance_tests_folder(request: FixtureRequest, tests_folder: Path) -> Path:
    return getattr(request, "param", tests_folder / "acceptance_tests")


@pytest.fixture(scope="session")
def data_folder(request: FixtureRequest, tests_folder: Path) -> Path:
    return getattr(request, "param", tests_folder / "data")


@pytest.fixture(scope="session")
def config_folder(request: FixtureRequest, tests_folder: Path) -> Path:
    return getattr(request, "param", tests_folder / "conf")


@pytest.fixture(scope="session")
def plugin_tests_folder(request: FixtureRequest, data_folder: Path) -> Path:
    return getattr(request, "param", data_folder / "plugin_tests")
