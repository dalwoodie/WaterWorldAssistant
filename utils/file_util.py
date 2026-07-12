"""
文件工具
"""

from pathlib import Path


class FileUtil:

    @staticmethod
    def ensure_dir(path):

        Path(path).mkdir(
            parents=True,
            exist_ok=True
        )