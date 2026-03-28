import logging

# Setup logging and dotenv by importing only
from .constants import LOGGER
from .rich import get_panel, setup_console

log = logging.getLogger(LOGGER)


def main():

    console = setup_console()
    panel = get_panel(console, "Hello", "Hello from coffee-helper-cli!")
    console.print(panel)


if __name__ == "__main__":
    main()
