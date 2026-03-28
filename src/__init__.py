"""Setup logging and dotenv for the project."""

from logging.config import dictConfig
from pathlib import Path
from typing import Any

import dotenv
import yaml

from .constants import CONFIG_DIR


def load_env() -> None:
    _ = dotenv.load_dotenv(override=True)


load_env()


def setup_logging() -> None:
    # Use script location to find config
    config_path: Path = CONFIG_DIR / "logging.yml"
    if not config_path.is_file():
        return

    config: dict[str, Any] | None = None  # pyright: ignore[reportAny]
    try:
        with open(config_path) as f:
            config = yaml.safe_load(f)
    except yaml.YAMLError:
        return
    else:
        if not config:
            return
        dictConfig(config)


setup_logging()
