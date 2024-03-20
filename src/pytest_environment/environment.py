"""Module containing the specification for a pytest Environment."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from _pytest.config import Config
from _pytest.nodes import Node


@dataclass(frozen=True)
class Environment:
    """Represents a collection of services that may be targeted by tests.

    Primarily allows parametrizing other fixtures by passing them config folders to reference.
    """

    config_folder: Path
    enable_command: str
    disable_command: str
    command_dest: str
    never_run_marker: str
    run_by_default: bool = False

    @classmethod
    def create_from_name(cls, name: str, config_folder: Path, **kwargs) -> Environment:
        """Create an Environment with defaults based off of the environments name.

        Can pass through kwargs to override defaults based on name.
        """
        return cls(
            config_folder=config_folder,
            enable_command=f"--{name}",
            disable_command=f"--no-{name}",
            command_dest=name,
            never_run_marker=f"no_{name}",
            **kwargs,
        )

    def should_run(self, node: Node) -> bool:
        """Checks if the environment should be run given the current context."""
        return self.is_enabled_by_cli(node.config) and not self.is_disabled_in_context(
            node
        )

    def is_enabled_by_cli(self, config: Config) -> bool:
        """Returns whether the environment is enabled by the CLI."""
        return config.getoption(name=self.command_dest)

    def is_disabled_in_context(self, node: Node) -> bool:
        """Returns whether the environment is permanently disabled in this context via the never_run_marker."""
        return node.get_closest_marker(name=self.never_run_marker) is not None
