from subprocess import run

from loguru import logger


def zabbix_sender(server, host, key, value):
    run(
        (
            "zabbix_sender",
            *("-z", server),
            *("-s", host),
            *("-k", key),
            *("-o", value),
        ),
        check=True,
    )


class ZabbixSilenceHandler:
    server: str
    host: str
    key: str

    def __init__(self, server, host, key):
        self.server = server
        self.host = host
        self.key = key

    def handle(self, event):
        if event.kind == "start":
            zabbix_sender(self.server, self.host, self.key, 1)
        elif event.kind == "end":
            zabbix_sender(self.server, self.host, self.key, 0)
