import pytest
from _pytest.fixtures import FixtureRequest


pytest_plugins: list[str] = ["pytest_environment.plugin"]


@pytest.fixture(scope="session")
def environment(request: FixtureRequest) -> None:
    return None


@pytest.fixture(scope="session")
def expected_environments() -> None:
    return None
