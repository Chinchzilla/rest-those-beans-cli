import logging
import sys
from typing import Any, TextIO

from rich.console import Console, Group
from rich.live import Live
from rich.panel import Panel
from rich.prompt import Prompt

from src.constants import LOGGER, MIN_CONSOLE_HEIGHT, MIN_CONSOLE_WIDTH

logger = logging.getLogger(LOGGER)


def get_panel(title: str, content: str, width: int, height: int) -> Panel:
    panel = Panel(content, title=title, width=width, height=height)
    return panel


def setup_console(io_file: TextIO = sys.stdout, console_args: dict[str, Any] = {}) -> Console:
    if console_args:
        for key, value in console_args.items():
            if not hasattr(Console, key):
                raise ValueError(f"Invalid console argument: {key}")
    return Console(file=io_file, force_terminal=True, **console_args)


def is_console_large_enough(console: Console) -> bool:
    """
    Measure the console size needed to render a given renderable.

    Args:
        console (Console): The console to measure.

    Returns:
        Bool that determines if the console is large enough to render the renderable.
    """
    size = console.size
    return size.width >= MIN_CONSOLE_WIDTH and size.height >= MIN_CONSOLE_HEIGHT
