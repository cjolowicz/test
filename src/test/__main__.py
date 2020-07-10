"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Test."""


if __name__ == "__main__":
    main(prog_name="test")  # pragma: no cover
