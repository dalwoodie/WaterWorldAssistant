"""
配置管理器

统一读取 config/*.yaml
"""

from pathlib import Path

import yaml


class Settings:

    def __init__(self):

        self.cache = {}

    def load(
        self,
        filename
    ):
        """
        读取yaml配置
        """

        path = Path("config") / filename

        if filename in self.cache:
            return self.cache[filename]

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            data = yaml.safe_load(f)

        self.cache[filename] = data

        return data

    def clear(self):
        """
        清除缓存
        """

        self.cache.clear()