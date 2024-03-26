from __future__ import annotations

from _pytest.config import Config


def test_pytest_addoption_with_dev(pytestconfig: Config) -> None:
    assert pytestconfig.getoption("dev", None) is True


def test_pytest_addoption_with_qa(pytestconfig: Config) -> None:
    assert pytestconfig.getoption("qa", None) is True


def test_pytest_addoption_with_prod(pytestconfig: Config) -> None:
    assert pytestconfig.getoption("prod", None) is True
