"""Sanity checks for repo config files: they must at least parse correctly."""
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent


def _load(path):
    with open(path) as f:
        return yaml.safe_load(f)


def test_dependabot_config_is_valid_yaml():
    config = _load(ROOT / ".github" / "dependabot.yml")

    assert config["version"] == 2
    assert config["updates"]


def test_workflow_files_are_valid_yaml():
    workflow_files = list((ROOT / ".github" / "workflows").glob("*.yml"))

    assert workflow_files, "expected at least one workflow file"
    for path in workflow_files:
        config = _load(path)
        assert "jobs" in config
