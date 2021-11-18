from pathlib import Path
from subprocess import Popen, run
from time import sleep

import pytest

here = Path(__file__).parent

from earhorn.earhorn import listen


@pytest.fixture
def howler():
    run(("make", "-C", here.parent, "howler-build"), check=True)

    with Popen(("make", "-C", here.parent, "howler-run")) as howler_process:
        sleep(2)
        yield "http://localhost:8000/howler.ogg"
        howler_process.kill()


def test_earhorn_listen(howler: str):
    listen(howler, silence=True)
