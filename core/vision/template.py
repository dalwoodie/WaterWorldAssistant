"""
模板管理器

统一管理 assets/templates 目录下所有模板图片。

功能：
    1. 加载模板
    2. 模板缓存
    3. 判断模板是否存在
"""

from pathlib import Path

import cv2


class TemplateManager:
    """
    模板管理器
    """

    ROOT = Path("assets/templates")

    def __init__(self):
        """
        初始化模板缓存
        """
        self._cache = {}

    def load(self, template_name: str):
        """
        加载模板

        Parameters
        ----------
        template_name
            模板名称，例如：

            buttons/back
            city/home
            resource/oil

        Returns
        -------
        numpy.ndarray
        """

        if template_name in self._cache:
            return self._cache[template_name]

        path = self.ROOT / f"{template_name}.png"

        if not path.exists():
            raise FileNotFoundError(
                f"模板不存在：{path}"
            )

        image = cv2.imread(str(path), cv2.IMREAD_COLOR)

        if image is None:
            raise RuntimeError(
                f"模板读取失败：{path}"
            )

        self._cache[template_name] = image

        return image

    def exists(self, template_name: str) -> bool:
        """
        判断模板是否存在
        """

        path = self.ROOT / f"{template_name}.png"

        return path.exists()

    def clear(self):
        """
        清空模板缓存
        """

        self._cache.clear()