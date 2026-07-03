"""
日志管理模块

整个项目统一使用这里提供的 logger。
"""

from pathlib import Path

from loguru import logger

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logger.remove()

logger.add(
    LOG_DIR / "latest.log",
    rotation="10 MB",
    retention="7 days",
    encoding="utf-8",
)

logger.add(
    sink=lambda msg: print(msg, end=""),
    colorize=True
)

__all__ = ["logger"]