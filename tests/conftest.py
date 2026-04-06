from io import StringIO

import pytest
from rich.console import Console


@pytest.fixture(scope="function")
def buffer() -> StringIO:
    return StringIO()


@pytest.fixture(scope="function")
def console(buffer) -> Console:
    return Console(file=buffer, force_terminal=True)
