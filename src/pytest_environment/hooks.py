"""Pytest hook specifications."""

from typing import Iterable

from _pytest.config import hookspec

from pytest_environment.environment import Environment


@hookspec
def pytest_environments() -> Iterable[Environment]:
    """Register environments for use in testing."""
