from _pytest.fixtures import FixtureRequest

from pytest_environment.environment import Environment
from pytest_environment.plugin import __iter_registered_environments


def test___iter_environments(
    request: FixtureRequest, expected_environments: list[Environment]
) -> None:
    environments: list[Environment] = [
        *__iter_registered_environments(request.config.pluginmanager)
    ]
    assert environments is not None
    for env in environments:
        assert isinstance(env, Environment)
    assert environments == expected_environments
