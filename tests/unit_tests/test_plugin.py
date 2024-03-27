from __future__ import annotations

from _pytest.config import ExitCode
from _pytest.pytester import Pytester
from _pytest.pytester import RunResult


def test_pytest_addhooks(
    pytester: Pytester, conftest_with_no_environments_content: str
) -> None:
    pytester.makeconftest(conftest_with_no_environments_content)
    pytester.copy_example("test_pytest_addhooks.py")
    result: RunResult = pytester.runpytest()
    result.assert_outcomes(passed=1)


def test___iter_registered_environments_with_no_environments(
    pytester: Pytester, conftest_with_no_environments_content: str
) -> None:
    pytester.makeconftest(conftest_with_no_environments_content)
    pytester.copy_example("test___iter_registered_environments.py")
    result: RunResult = pytester.runpytest()
    result.assert_outcomes(passed=1)


class TestPytestAddoption:
    def test_pytest_addoption_with_no_environments(
        self, pytester: Pytester, conftest_with_no_environments_content: str
    ) -> None:
        pytester.makeconftest(conftest_with_no_environments_content)
        pytester.copy_example("test_pytest_addoption.py")

        assert pytester.runpytest("--dev").ret == ExitCode.USAGE_ERROR
        assert pytester.runpytest("--no-dev").ret == ExitCode.USAGE_ERROR
        assert pytester.runpytest("--qa").ret == ExitCode.USAGE_ERROR
        assert pytester.runpytest("--no-qa").ret == ExitCode.USAGE_ERROR
        assert pytester.runpytest("--prod").ret == ExitCode.USAGE_ERROR
        assert pytester.runpytest("--no-prod").ret == ExitCode.USAGE_ERROR

    def test_pytest_addoption_with_one_environment(
        self, pytester: Pytester, conftest_with_one_environment_content: str
    ) -> None:
        pytester.makeconftest(conftest_with_one_environment_content)
        pytester.copy_example("test_pytest_addoption.py")
        pytester.runpytest().assert_outcomes(failed=3)
        pytester.runpytest("--dev").assert_outcomes(passed=1, failed=2)
        pytester.runpytest("--no-dev").assert_outcomes(failed=3)
        assert pytester.runpytest("--qa").ret == ExitCode.USAGE_ERROR
        assert pytester.runpytest("--no-qa").ret == ExitCode.USAGE_ERROR
        assert pytester.runpytest("--prod").ret == ExitCode.USAGE_ERROR
        assert pytester.runpytest("--no-prod").ret == ExitCode.USAGE_ERROR

    def test_pytest_addoption_with_many_environments(
        self, pytester: Pytester, conftest_with_many_environments_content: str
    ) -> None:
        pytester.makeconftest(conftest_with_many_environments_content)
        pytester.copy_example("test_pytest_addoption.py")
        pytester.runpytest().assert_outcomes(failed=3)
        pytester.runpytest("--dev").assert_outcomes(passed=1, failed=2)
        pytester.runpytest("--no-dev").assert_outcomes(failed=3)
        pytester.runpytest("--qa").assert_outcomes(passed=1, failed=2)
        pytester.runpytest("--no-qa").assert_outcomes(failed=3)
        pytester.runpytest("--prod").assert_outcomes(passed=1, failed=2)
        pytester.runpytest("--no-prod").assert_outcomes(failed=3)

    def test_pytest_addoption_with_duplicate_environments(
        self, pytester: Pytester, conftest_with_duplicate_environments_content: str
    ) -> None:
        pytester.makeconftest(conftest_with_duplicate_environments_content)
        pytester.copy_example("test_pytest_addoption.py")
        pytester.runpytest().assert_outcomes(failed=3)
        pytester.runpytest("--dev").assert_outcomes(passed=1, failed=2)
        pytester.runpytest("--no-dev").assert_outcomes(failed=3)
        pytester.runpytest("--qa").assert_outcomes(passed=1, failed=2)
        pytester.runpytest("--no-qa").assert_outcomes(failed=3)
        assert pytester.runpytest("--prod").ret == ExitCode.USAGE_ERROR
        assert pytester.runpytest("--no-prod").ret == ExitCode.USAGE_ERROR


class TestPytestConfigure:
    def test_pytest_configure_with_no_environments(
        self, pytester: Pytester, conftest_with_no_environments_content: str
    ) -> None:
        pytester.makeconftest(conftest_with_no_environments_content)
        pytester.copy_example("test_pytest_configure.py")
        pytester.runpytest().assert_outcomes(failed=3)

    def test_pytest_configure_with_one_environment(
        self, pytester: Pytester, conftest_with_one_environment_content: str
    ) -> None:
        pytester.makeconftest(conftest_with_one_environment_content)
        pytester.copy_example("test_pytest_configure.py")
        pytester.runpytest().assert_outcomes(passed=1, failed=2)

    def test_pytest_configure_with_many_environments(
        self, pytester: Pytester, conftest_with_many_environments_content: str
    ) -> None:
        pytester.makeconftest(conftest_with_many_environments_content)
        pytester.copy_example("test_pytest_configure.py")
        pytester.runpytest().assert_outcomes(passed=3)

    def test_pytest_configure_with_duplicate_environments(
        self, pytester: Pytester, conftest_with_duplicate_environments_content: str
    ) -> None:
        pytester.makeconftest(conftest_with_duplicate_environments_content)
        pytester.copy_example("test_pytest_configure.py")
        pytester.runpytest().assert_outcomes(passed=2, failed=1)


class TestPytestPycollectMakeitem:
    def test_pytest_pycollect_makeitem_with_no_environments(
        self, pytester: Pytester, conftest_with_no_environments_content: str
    ) -> None:
        pytester.makeconftest(conftest_with_no_environments_content)
        pytester.copy_example("test_pytest_pycollect_makeitem.py")
        pytester.runpytest().assert_outcomes(passed=0, skipped=1)

    def test_pytest_pycollect_makeitem_with_one_environment(
        self, pytester: Pytester, conftest_with_one_environment_content: str
    ) -> None:
        pytester.makeconftest(conftest_with_one_environment_content)
        pytester.copy_example("test_pytest_pycollect_makeitem.py")
        pytester.runpytest().assert_outcomes(passed=1, skipped=0)

    def test_pytest_pycollect_makeitem_with_many_environments(
        self, pytester: Pytester, conftest_with_many_environments_content: str
    ) -> None:
        pytester.makeconftest(conftest_with_many_environments_content)
        pytester.copy_example("test_pytest_pycollect_makeitem.py")
        pytester.runpytest().assert_outcomes(passed=3, skipped=0)

    def test_pytest_pycollect_makeitem_with_duplicate_environments(
        self, pytester: Pytester, conftest_with_duplicate_environments_content: str
    ) -> None:
        pytester.makeconftest(conftest_with_duplicate_environments_content)
        pytester.copy_example("test_pytest_pycollect_makeitem.py")
        pytester.runpytest().assert_outcomes(passed=2, skipped=0)


class TestPytestGenerateTests:
    def test_pytest_generate_tests_with_no_environments(
        self, pytester: Pytester, conftest_with_no_environments_content: str
    ) -> None:
        pytester.makeconftest(conftest_with_no_environments_content)
        pytester.copy_example("test_pytest_generate_tests.py")
        pytester.runpytest().assert_outcomes(skipped=3)

    def test_pytest_generate_tests_with_one_environment(
        self, pytester: Pytester, conftest_with_one_environment_content: str
    ) -> None:
        pytester.makeconftest(conftest_with_one_environment_content)
        pytester.copy_example("test_pytest_generate_tests.py")
        pytester.runpytest("--dev").assert_outcomes(passed=2, skipped=1)

    def test_pytest_generate_tests_with_many_environments(
        self, pytester: Pytester, conftest_with_many_environments_content: str
    ) -> None:
        pytester.makeconftest(conftest_with_many_environments_content)
        pytester.copy_example("test_pytest_generate_tests.py")
        pytester.runpytest("--dev").assert_outcomes(passed=6)
        pytester.runpytest("--qa").assert_outcomes(passed=6)
        pytester.runpytest("--prod").assert_outcomes(passed=6)

    def test_pytest_generate_tests_with_duplicate_environments(
        self, pytester: Pytester, conftest_with_duplicate_environments_content: str
    ) -> None:
        pytester.makeconftest(conftest_with_duplicate_environments_content)
        pytester.copy_example("test_pytest_generate_tests.py")
        pytester.runpytest("--dev").assert_outcomes(passed=4)
        pytester.runpytest("--qa").assert_outcomes(passed=4)
