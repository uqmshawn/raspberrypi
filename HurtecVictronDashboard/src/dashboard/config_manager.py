"""Configuration loader and saver.

The application stores its runtime configuration in ``config.json`` in the
current working directory.  If that file does not exist, ``default_config.json``
from the top level ``config`` directory is loaded instead.
"""

import json
from pathlib import Path

CONFIG_FILE = Path("config.json")
DEFAULT_CONFIG = Path(__file__).resolve().parents[2] / "config" / "default_config.json"


def load_config():
    """Load configuration from disk.

    Returns a dictionary containing the configuration.  The default configuration
    is loaded when no user configuration is present.
    """

    path = CONFIG_FILE if CONFIG_FILE.exists() else DEFAULT_CONFIG
    if path.exists():
        with path.open() as f:
            return json.load(f)
    return {}


def save_config(data):
    """Persist configuration to ``config.json``."""

    with CONFIG_FILE.open("w") as f:
        json.dump(data, f, indent=2)
