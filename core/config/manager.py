from pathlib import Path

import yaml


class ConfigManager:

    def __init__(self):

        self.path = Path("config/config.yaml")

        with open(
            self.path,
            "r",
            encoding="utf-8"
        ) as f:

            self.data = yaml.safe_load(f)

    def get(self, *keys):

        value = self.data

        for key in keys:

            value = value[key]

        return value