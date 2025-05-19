import uuid

from pytest_environment.environment import Environment


def test_environment_create_from_name() -> None:
    env_name: str = str(uuid.uuid4())
    env: Environment = Environment.create_from_name(name=env_name)
    assert env is not None
    assert isinstance(env, Environment)
    assert env.config_fixture == env_name + "_config_path"
    assert env.enable_command == "--" + env_name
    assert env.disable_command == "--no-" + env_name
    assert env.command_dest == env_name
    assert env.never_run_marker == "no_" + env_name
