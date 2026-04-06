import logging
import sys
from typing import Any, TextIO

from rich.console import Console, Group
from rich.live import Live
from rich.panel import Panel
from rich.prompt import Prompt

from src.constants import LOGGER

logger = logging.getLogger(LOGGER)


def get_panel(title: str, content: str, width: int, height: int) -> Panel:
    panel = Panel(content, title=title, width=width, height=height)
    return panel


def setup_console(io_file: TextIO = sys.stdout, console_args: dict[str, Any] = {}) -> Console:
    if console_args:
        for key in console_args.keys():
            if not hasattr(Console, key):
                raise ValueError(f"Invalid console argument: {key}")
    return Console(file=io_file, force_terminal=True, stderr=False, **console_args)
