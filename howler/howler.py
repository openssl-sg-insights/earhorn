#!/usr/bin/env python3

from subprocess import Popen, run
from time import sleep
from threading import Thread
from queue import Queue


class Howler(Thread):
    queue: Queue

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        with Popen(["icecast", "-c", "./icecast.xml"]) as icecast_process:
            for item in self.queue:
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
                self.queue.task_done()
