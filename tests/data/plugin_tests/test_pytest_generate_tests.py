from _pytest.fixtures import FixtureRequest

from pytest_environment.environment import Environment


def test_pytest_generate_tests_with_dev(
    request: FixtureRequest, environment: Environment
) -> None:
    assert environment.command_dest != "dev"
    assert request.node.get_closest_marker("no_dev") is not None


def test_pytest_generate_tests_with_qa(
    request: FixtureRequest, environment: Environment
) -> None:
    assert environment.command_dest != "qa"
    assert request.node.get_closest_marker("no_qa") is not None


def test_pytest_generate_tests_with_prod(
    request: FixtureRequest, environment: Environment
) -> None:
    assert environment.command_dest != "prod"
    assert request.node.get_closest_marker("no_prod") is not None
