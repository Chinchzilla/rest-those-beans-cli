import pytest
from rich.panel import Panel
from src.cli import get_panel, is_console_large_enough, setup_console


def test_get_panel():
    panel = get_panel("Title", "Content", 93, 34)
    assert panel is not None
    assert isinstance(panel, Panel)
    assert panel.width == 93
    assert panel.height == 34
    assert panel.renderable == "Content"
    assert panel.title == "Title"
    assert panel.border_style == "none"
    assert panel.style == "none"
    assert panel.padding == (0, 1)
    assert panel.expand is True
    assert panel.highlight is False


class TestConsole:
    @pytest.mark.parametrize(
        "console_scope_function", [{"width": 93, "height": 34}, {"width": 100, "height": 48}], indirect=True
    )
    def test_console_large_enough(self, console_scope_function):
        assert is_console_large_enough(console_scope_function)

    @pytest.mark.parametrize(
        "console_scope_function",
        [{"width": 83, "height": 48}, {"width": 100, "height": 23}, {"width": 72, "height": 12}],
        indirect=True,
    )
    def test_console_not_large_enough(self, console_scope_function):
        assert not is_console_large_enough(console_scope_function)

    @pytest.mark.parametrize(
        "invalid_console_args",
        [{"wdth": 82, "height": 48}, {"width": 82, "heigh": 48}],
    )
    def test_console_setup_raises_attribute_error(self, buffer_scope_function, invalid_console_args):
        with pytest.raises(ValueError):
            setup_console(io_file=buffer_scope_function, console_args=invalid_console_args)

    @pytest.mark.parametrize(
        "invalid_console_args",
        [{"width": True, "height": "this"}],
    )
    def test_console_setup_raises_type_error(self, buffer_scope_function, invalid_console_args):
        with pytest.raises(TypeError):
            setup_console(io_file=buffer_scope_function, console_args=invalid_console_args)
