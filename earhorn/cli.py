import click

from .archive import TIMESTAMP_FORMAT
from .earhorn import listen


@click.command()
@click.option(
    "--silence",
    envvar="SILENCE",
    help="Enable silence monitoring.",
    is_flag=True,
    default=False,
)
@click.option(
    "--silence-threshold",
    envvar="SILENCE_THRESHOLD",
    help="Duration of a silence before alerting.",
    default=5,
)
@click.option(
    "--silence-handler-logs",
    envvar="SILENCE_HANDLER_LOGS",
    help="Path to the silence handler logs.",
)
@click.option(
    "--archive-path",
    envvar="ARCHIVE_PATH",
    help="Path to the archive directory.",
    type=click.Path(),
)
@click.option(
    "--archive-segment-size",
    envvar="ARCHIVE_SEGMENT_SIZE",
    help="Archive segment size in seconds.",
    default=3600,
)
@click.option(
    "--archive-segment-filename",
    envvar="ARCHIVE_SEGMENT_FILENAME",
    help="Archive segment filename.",
    default=f"archive-{TIMESTAMP_FORMAT}.ogg",
)
@click.option(
    "--archive-segment-format",
    envvar="ARCHIVE_SEGMENT_FORMAT",
    help="Archive segment format.",
    default="ogg",
)
@click.argument(
    "url",
    envvar="URL",
)
def run(**kwargs):
    """
    URL of the stream.
    """
    listen(**kwargs)
