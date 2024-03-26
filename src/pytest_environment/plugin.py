"""Module that will be used as the entry point for the pytest-environment plugin."""

from __future__ import annotations

from typing import Generator
from typing import Iterable

import pytest
from _pytest.config import Config
from _pytest.config import PytestPluginManager
from _pytest.config.argparsing import Parser
from _pytest.fixtures import FixtureRequest
from _pytest.nodes import Collector
from _pytest.nodes import Item
from _pytest.python import Class
from _pytest.python import Metafunc
from _pytest.python import Module

from pytest_environment.environment import Environment


CLI_OPTION_PREFIX: str = "--"


def pytest_addhooks(pluginmanager: PytestPluginManager) -> None:
    """Pytest hook used for adding new hooks."""
    from pytest_environment import hooks

    pluginmanager.add_hookspecs(hooks)


def __retrieve_unique_environments(
    pluginmanager: PytestPluginManager,
) -> Iterable[Environment]:
    """Returns all unique registered environments."""
    found_environments: list[Environment] = list(
        __iter_registered_environments(pluginmanager=pluginmanager)
    )
    unique_registered_environments: list[Environment] = []
    for env in found_environments:
        if env not in unique_registered_environments:
            # Uses roundabout list appending to maintain the order.
            unique_registered_environments.append(env)

    return unique_registered_environments


def __iter_registered_environments(
    pluginmanager: PytestPluginManager,
) -> Generator[Environment, None, None]:
    """Iterates over all registered environments."""
    for registered_envs in pluginmanager.hook.pytest_environments():
        yield from registered_envs


def pytest_addoption(parser: Parser, pluginmanager: PytestPluginManager) -> None:
    """Pytest hook for adding to the CLI."""
    for environment in __retrieve_unique_environments(pluginmanager=pluginmanager):
        parser.addoption(
            environment.enable_command,
            action="store_true",
            dest=environment.command_dest,
            default=environment.run_by_default,
        )
        parser.addoption(
            environment.disable_command,
            action="store_false",
            dest=environment.command_dest,
            default=not environment.run_by_default,
        )


def pytest_configure(config: Config) -> None:
    """Pytest hook used for configuration."""
    if not config.pluginmanager.hasplugin("pytest_repo_structure"):
        config.pluginmanager.register("pytest_repo_structure")

    for env in __retrieve_unique_environments(pluginmanager=config.pluginmanager):
        config.addinivalue_line(
            name="markers",
            line=f"{env.never_run_marker}: Marks the current context to not allow running tests"
            f" in the {env.enable_command} environment",
        )


def pytest_pycollect_makeitem(
    collector: Module | Class,
) -> Item | Collector | list[Item | Collector] | None:
    """Pytest hook for hooking into module and class collections."""
    if isinstance(collector, Module):
        if "unit_tests" in collector.path.parts:
            for marker in ["no_dev", "no_qa", "no_prod"]:
                collector.add_marker(marker)
        if "integration_tests" in collector.path.parts:
            collector.add_marker("no_docker")
    return None


def pytest_generate_tests(metafunc: Metafunc) -> None:
    """Pytest hook for altering the tests being generated."""
    if "environment" in metafunc.fixturenames:
        registered_envs: Iterable[Environment] = __retrieve_unique_environments(
            pluginmanager=metafunc.config.pluginmanager
        )
        possible_environments: Iterable[Environment] = [
            env
            for env in registered_envs
            if metafunc.definition.get_closest_marker(env.never_run_marker) is None
        ]

        metafunc.parametrize(
            argnames="environment",
            argvalues=possible_environments,
            ids=[
                env.enable_command.lstrip(CLI_OPTION_PREFIX)
                for env in possible_environments
            ],
        )


@pytest.fixture(scope="session")
def environment(request: FixtureRequest) -> Environment:
    """Parametrized fixture that returns currently relevant Environment instances."""
    env: Environment | None = getattr(request, "param", None)
    if env is None:
        raise pytest.UsageError(
            "Failed to parametrize environment with the Environments instances."
        )
    if not env.is_enabled_by_cli(config=request.config):
        pytest.skip(
            f"Skipping {env.enable_command.lower().lstrip(CLI_OPTION_PREFIX)} due to being disabled."
        )

    return env
