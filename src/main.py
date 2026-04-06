import logging

from src.cli import get_panel, setup_console
from src.constants import LOGGER

log = logging.getLogger(LOGGER)


def main():

    console = setup_console()
    panel = get_panel(
        title="Hello",
        content="Hello from coffee-helper-cli!",
        width=round(console.width * 0.70),
        height=round(console.height * 0.90),
    )
    console.print(panel)


if __name__ == "__main__":
    main()
