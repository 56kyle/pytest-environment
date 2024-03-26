from pytest_environment.environment import Environment


def test_pytest_pycollect_makeitem(environment: Environment) -> None:
    assert environment is not None
