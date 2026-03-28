import logging
import sys
from typing import TextIO

from rich.console import Console, Group
from rich.live import Live
from rich.panel import Panel
from rich.prompt import Prompt

from .constants import LOGGER

logger = logging.getLogger(LOGGER)


def get_panel(console: Console, title: str, content: str) -> Panel:
    panel = Panel(content, title=title)
    return panel


def setup_console(io_file: TextIO = sys.stdout) -> Console:
    console = Console(file=io_file)
    return console
