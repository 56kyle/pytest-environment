"""Fixtures used in unit tests."""

from pathlib import Path

import pytest
from _pytest.fixtures import FixtureRequest


@pytest.fixture(scope="session")
def conftest_with_no_environments_content(
    request: FixtureRequest, conftest_with_no_environments_path: Path
) -> str:
    return getattr(request, "param", conftest_with_no_environments_path.read_text())


@pytest.fixture(scope="session")
def conftest_with_no_environments_path(
    request: FixtureRequest, plugin_tests_folder: Path
) -> Path:
    return getattr(
        request, "param", plugin_tests_folder / "conftest_with_no_environments.py"
    )


@pytest.fixture(scope="session")
def conftest_with_one_environment_content(
    request: FixtureRequest, conftest_with_one_environment_path: Path
) -> str:
    return getattr(request, "param", conftest_with_one_environment_path.read_text())


@pytest.fixture(scope="session")
def conftest_with_one_environment_path(
    request: FixtureRequest, plugin_tests_folder: Path
) -> Path:
    return getattr(
        request, "param", plugin_tests_folder / "conftest_with_one_environment.py"
    )


@pytest.fixture(scope="session")
def conftest_with_many_environments_content(
    request: FixtureRequest, conftest_with_many_environments_path: Path
) -> str:
    return getattr(request, "param", conftest_with_many_environments_path.read_text())


@pytest.fixture(scope="session")
def conftest_with_many_environments_path(
    request: FixtureRequest, plugin_tests_folder: Path
) -> Path:
    return getattr(
        request, "param", plugin_tests_folder / "conftest_with_many_environments.py"
    )


@pytest.fixture(scope="session")
def conftest_with_duplicate_environments_content(
    request: FixtureRequest, conftest_with_duplicate_environments_path: Path
) -> str:
    return getattr(
        request, "param", conftest_with_duplicate_environments_path.read_text()
    )


@pytest.fixture(scope="session")
def conftest_with_duplicate_environments_path(
    request: FixtureRequest, plugin_tests_folder: Path
) -> Path:
    return getattr(
        request,
        "param",
        plugin_tests_folder / "conftest_with_duplicate_environments.py",
    )


@pytest.fixture(scope="session")
def conftest_with_overriden_environment_content(
    request: FixtureRequest, conftest_with_overridden_environment_path: Path
) -> str:
    return getattr(
        request, "param", conftest_with_overridden_environment_path.read_text()
    )


@pytest.fixture(scope="session")
def conftest_with_overridden_environment_path(
    request: FixtureRequest, plugin_tests_folder: Path
) -> Path:
    return getattr(
        request,
        "param",
        plugin_tests_folder / "conftest_with_overridden_environment.py",
    )
