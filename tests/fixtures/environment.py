import uuid

import pytest
from _pytest.fixtures import FixtureRequest

from pytest_environment.environment import Environment


@pytest.fixture(scope="function")
def environment(
    request: FixtureRequest,
    environment__config_fixture: str,
    environment__enable_command: str,
    environment__disable_command: str,
    environment__command_dest: str,
    environment__never_run_marker: str,
    environment__run_by_default: bool,
) -> Environment:
    return getattr(
        request,
        "param",
        Environment(
            config_fixture=environment__config_fixture,
            enable_command=environment__enable_command,
            disable_command=environment__disable_command,
            command_dest=environment__command_dest,
            never_run_marker=environment__never_run_marker,
            run_by_default=environment__run_by_default,
        ),
    )


@pytest.fixture(scope="function")
def environment__config_fixture(request: FixtureRequest) -> str:
    return getattr(request, "param", str(uuid.uuid4()) + "_config_fixture")


@pytest.fixture(scope="function")
def environment__enable_command(request: FixtureRequest) -> str:
    return getattr(request, "param", str(uuid.uuid4()))


@pytest.fixture(scope="function")
def environment__disable_command(request: FixtureRequest) -> str:
    return getattr(request, "param", str(uuid.uuid4()))


@pytest.fixture(scope="function")
def environment__command_dest(request: FixtureRequest) -> str:
    return getattr(request, "param", str(uuid.uuid4()))


@pytest.fixture(scope="function")
def environment__never_run_marker(request: FixtureRequest) -> str:
    return getattr(request, "param", str(uuid.uuid4()))


@pytest.fixture(scope="function")
def environment__run_by_default(request: FixtureRequest) -> bool:
    return getattr(request, "param", False)
