from pathlib import Path
from typing import Optional

import typer

from build import build

app = typer.Typer()


@app.command()
def main(
    entrypoint: Optional[Path] = typer.Option(
        'main.py', '--entrypoint', '-e', help="Path to the entrypoint file."
    )
):
    if entrypoint.exists():
        typer.echo(f"{entrypoint} founded.")
        build(entrypoint)
    else:
        typer.echo(f"File does not exist: {entrypoint}")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
