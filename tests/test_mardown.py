import sys
from io import StringIO

from rich.console import Console
from rich.markdown import Markdown
from rich.text import Text


class TestMarkdown:
    def test_makrdown(self):
        markdown = """
# Title
## Subtitle
### Subsubtitle
#### Subsubsubtitle
##### Subsubsubsubtitle
###### Subsubsubsubsubtitle

_Lorem_ ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

- Item 1
- Item 2

1. Item 1
2. Item 2
        """
        console = Console()
        console.print(Markdown(markdown))

    def test_markdown_with_markup_colours(self):
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
        buffer = StringIO()
        console = Console(file=buffer, force_terminal=True)
        console.print(Markdown(markdown))
        capture = buffer.getvalue()
        console.file = sys.stdout
        text = Text.from_markup(capture)
        console.print(text)
