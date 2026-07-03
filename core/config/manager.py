"""
配置管理器
"""

from pathlib import Path

import yaml


class ConfigManager:

    def __init__(self):

        self.config_path = Path("config/config.yaml")

        self.data = self.load()

    def load(self):

        with open(self.config_path, encoding="utf-8") as f:

            return yaml.safe_load(f)

    def get(self, *keys):

        value = self.data

        for key in keys:

            value = value[key]

        return value