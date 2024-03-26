from pytest_environment.environment import Environment


def test_environment(
    environment: Environment, expected_environments: list[Environment]
) -> None:
    assert environment is not None
    assert isinstance(environment, Environment)
    assert environment in expected_environments


def test_environment_with_overridden_fixture(
    environment: Environment, expected_environments: None
) -> None:
    assert environment == expected_environments
    assert environment is None
