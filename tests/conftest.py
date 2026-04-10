from io import StringIO

import pytest
from rich.console import Console
from src.cli import setup_console


@pytest.fixture(scope="function")
def buffer_scope_function() -> StringIO:
    return StringIO()


@pytest.fixture(scope="function")
def console_scope_function(buffer_scope_function, request) -> Console:
    return setup_console(io_file=buffer_scope_function, console_args=request.param if hasattr(request, "param") else {})
