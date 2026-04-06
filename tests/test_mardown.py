from rich.markdown import Markdown
from rich.text import Text


class TestMarkdown:
    def test_makrdown(self, console, buffer):
        markdown = """
# Title
## Subtitle
### Subsubtitle
#### Subsubsubtitle
##### Subsubsubsubtitle
###### Subsubsubsubsubtitle

_Lorem_ ipsum dolor sit amet, consectetur adipiscing **elit**, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

- Item 1
- Item 2

1. Item 1
2. Item 2
        """
        console.print(Markdown(markdown))
        captured: str = buffer.getvalue()

        assert "\x1b[1;4mTitle\x1b[0m" in captured
        assert "\x1b[4;35mSubtitle\x1b[0m" in captured
        assert "\x1b[3;35mSubsubsubtitle\x1b[0m" in captured
        assert "\x1b[3mSubsubsubsubtitle\x1b[0m" in captured
        assert "\x1b[2mSubsubsubsubsubtitle\x1b[0m" in captured
        assert "\x1b[3mLorem\x1b[0m" in captured
        assert "\x1b[1m • \x1b[0mItem 1" in captured
        assert "\x1b[1m • \x1b[0mItem 2" in captured
        assert "\x1b[36m 1 \x1b[0mItem 1" in captured
        assert "\x1b[36m 2 \x1b[0mItem 2" in captured

    def test_markdown_with_markup_colours(self, console, buffer):
        markdown = """
# Title
## Subtitle
### Subsubtitle
#### Subsubsubtitle
##### Subsubsubsubtitle
###### Subsubsubsubsubtitle

[red][italic]Lorem[/red] ipsum dolor[/italic] sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

- [blue]Item 1[/]
- Item 2

1. Item 1
2. Item 2
        """
        console.print(Markdown(markdown))
        capture = buffer.getvalue()
        text = Text.from_ansi(capture)
        assert "[red][italic]Lorem[/red] ipsum dolor[/italic]" in text
        assert "[blue]Item 1[/]" in text
