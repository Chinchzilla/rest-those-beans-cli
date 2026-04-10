from pathlib import Path

# Paths
USER_HOME_DIR: Path = Path.home()
DOTENV_PATH: Path = USER_HOME_DIR.joinpath(".env")
PROJECT_ROOT_DIR: Path = Path(__file__).parents[1]
SRC: Path = PROJECT_ROOT_DIR.joinpath("src")
CONFIG_DIR: Path = PROJECT_ROOT_DIR.joinpath("conf")

LOGGER: str = "coffee_helper"

EIGHTY_PERCENT: float = 80 / 100
MIN_CONSOLE_WIDTH: int = 90
MIN_CONSOLE_HEIGHT: int = 30
