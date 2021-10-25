#!/usr/bin/env python3

from subprocess import Popen, run
from time import sleep
from threading import thread


def icecast():
    with Popen(["icecast", "-c", "./icecast.xml"]) as icecast_process:
        yield
        icecast_process.kill()


def stream_sample():
    run(
        (
            *("ffmpeg", "-hide_banner", "-nostats"),
            "-re",
            *("-i", "sample.ogg"),
            *("-f", "ogg"),
            *("-content_type", "audio/ogg"),
            "icecast://source:hackme@localhost:8000/howler.ogg",
        ),
        check=True,
    )
