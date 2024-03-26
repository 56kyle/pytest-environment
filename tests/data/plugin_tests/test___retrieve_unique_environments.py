from _pytest.fixtures import FixtureRequest

from pytest_environment.environment import Environment
from pytest_environment.plugin import __retrieve_unique_environments


def test___retrieve_environments(
    request: FixtureRequest, expected_environments: list[Environment]
) -> None:
    environments: list[Environment] = [
        *__retrieve_unique_environments(request.config.pluginmanager)
    ]
    assert environments
    for env in environments:
        assert isinstance(env, Environment)
    assert environments == expected_environments
