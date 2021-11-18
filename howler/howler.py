#!/usr/bin/env python3

from subprocess import Popen, run
from time import sleep


def main():
    with Popen(["icecast", "-c", "/etc/icecast/icecast.xml"]) as icecast:
        sleep(1)
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
        sleep(5)
        icecast.kill()


main()
