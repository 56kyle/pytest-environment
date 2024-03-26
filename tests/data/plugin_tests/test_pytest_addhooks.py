from _pytest.config import Config


def test_pytest_addhooks(pytestconfig: Config) -> None:
    assert pytestconfig.hook.pytest_environments is not None
