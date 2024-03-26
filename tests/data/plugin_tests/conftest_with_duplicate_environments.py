from typing import Iterable

import pytest

from pytest_environment.environment import Environment


pytest_plugins: list[str] = ["pytest_environment.plugin"]


ENVIRONMENTS: list[Environment] = [
    Environment.create_from_name("dev"),
    Environment.create_from_name("qa"),
    Environment.create_from_name("qa"),
]


def pytest_environments() -> Iterable[Environment]:
    return ENVIRONMENTS


@pytest.fixture(scope="session")
def expected_environments() -> Iterable[Environment]:
    return ENVIRONMENTS
