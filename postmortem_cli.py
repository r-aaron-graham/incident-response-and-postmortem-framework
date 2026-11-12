"""CLI to generate new incident reports from a template."""

from __future__ import annotations

import datetime
from pathlib import Path

import click


TEMPLATE_PATH = Path(__file__).resolve().parent / "templates" / "incident.md"


@click.command()
@click.option("--id", required=True, help="Incident identifier (e.g. INC-12345).")
@click.option("--title", required=True, help="Short title for the incident.")
@click.option(
    "--output", type=click.Path(dir_okay=False, path_type=Path), required=True, help="Path to write the new incident report."
)
def main(id: str, title: str, output: Path):
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    date = datetime.date.today().isoformat()
    content = template.replace("{{ id }}", id).replace("{{ title }}", title).replace("{{ date }}", date)
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        with output.open("x", encoding="utf-8") as report:
            report.write(content)
    except FileExistsError as exc:
        raise click.ClickException(f"Report already exists: {output}") from exc
    click.echo(f"Created incident report at {output}")


if __name__ == "__main__":  # pragma: no cover
    main()