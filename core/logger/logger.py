"""
日志模块

统一输出：

INFO

WARNING

ERROR

DEBUG
"""

import logging

from pathlib import Path


class Logger:

    _logger = None

    @classmethod
    def get(cls):

        if cls._logger:

            return cls._logger

        Path("logs").mkdir(
            exist_ok=True
        )

        logger = logging.getLogger(
            "WaterWorld"
        )

        logger.setLevel(
            logging.INFO
        )

        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s - %(message)s"
        )

        console = logging.StreamHandler()

        console.setFormatter(
            formatter
        )

        file = logging.FileHandler(
            "logs/latest.log",
            encoding="utf-8"
        )

        file.setFormatter(
            formatter
        )

        logger.addHandler(
            console
        )

        logger.addHandler(
            file
        )

        cls._logger = logger

        return logger