from pathlib import Path

from loguru import logger

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logger.remove()

logger.add(
    LOG_DIR / "latest.log",
    level="DEBUG",
    encoding="utf-8",
    rotation="10 MB",
)

logger.add(
    lambda msg: print(msg, end="")
)