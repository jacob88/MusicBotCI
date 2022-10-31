import typer
from pathlib import Path
from typer import Argument, Option
from rich import print
from .actions import tag_pom

app = typer.Typer(
    name="MusicBotCI",
    context_settings={
        "help_option_names": ['-h', '--help'],
    },
)


@app.callback()
def callback():
    """
    Awesome Portal Gun
    """


@app.command(
    name="tag-pom",
    short_help="Updates POM project version, ready for a new release.",
)
def tag_pom_cmd(
    version: str = Argument(
        help="New version to write to POM project file.",
        show_default=False,
        default=...,
    ),
    file: Path = Option(
        help="Path to POM project file.",
        exists=True,
        writable=True,
        readable=True,
        resolve_path=True,
        *("./pom.xml", "-f", "--file")
    ),
):
    """Updates POM project file (pom.xml) with version string passed to command."""

    print(f":floppy_disk: Saving project version to [bold]({file.name})[bold]")
    tag_pom(version, file)
    print("[bold green]:heavy_check_mark: Version updated successfully![bold green]")
