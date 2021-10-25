from .logging import create_task_logger
from pathlib import Path


class LogsSilenceHandler:
    filepath: Path
    serialize: bool = False

    def __init__(self, filepath, serialize):
        self.filepath = filepath
        self.serialize = serialize

        self.logger = create_task_logger(
            self.filepath,
            self.serialize,
        )

    def handle(self, event):
        self.logger.info(event)
