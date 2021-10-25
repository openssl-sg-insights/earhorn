from copy import deepcopy
from pathlib import Path
from typing import TYPE_CHECKING
from loguru import logger

if TYPE_CHECKING:
    from loguru import Logger


_empty_logger = deepcopy(logger)


def create_task_logger(
    filepath: Path,
    serialize: bool = False,
) -> "Logger":
    task_logger = deepcopy(_empty_logger)
    task_logger.configure(
        handlers=[dict(sink=filepath, enqueue=True, serialize=serialize)],
    )

    return task_logger
