"""Pytest hook specifications."""

from typing import Iterable

from _pytest.config import hookspec

from pytest_environment.environment import Environment


@hookspec
def register_environments() -> Iterable[Environment]:
    """Hook for registering environments."""
