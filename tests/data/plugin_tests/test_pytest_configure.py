from _pytest.config import Config


def test_pytest_configure_has_no_dev_marker(pytestconfig: Config) -> None:
    assert "no_dev" in "".join(pytestconfig.getini("markers"))


def test_pytest_configure_has_no_qa_marker(pytestconfig: Config) -> None:
    assert "no_qa" in "".join(pytestconfig.getini("markers"))


def test_pytest_configure_has_no_prod_marker(pytestconfig: Config) -> None:
    assert "no_prod" in "".join(pytestconfig.getini("markers"))
