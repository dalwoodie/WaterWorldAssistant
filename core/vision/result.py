"""
Vision识别结果对象

统一封装：

1. 模板匹配
2. OCR识别
3. 后续颜色识别

所有视觉模块统一返回 VisionResult。
"""

from dataclasses import dataclass
from typing import List


@dataclass
class OCRBox:
    """
    OCR单个文本框
    """

    text: str

    confidence: float

    x: int

    y: int

    width: int

    height: int

    def center(self):
        """
        返回文本框中心坐标
        """

        return (
            self.x + self.width // 2,
            self.y + self.height // 2
        )


@dataclass
class VisionResult:
    """
    通用视觉识别结果
    """

    found: bool

    x: int = 0

    y: int = 0

    width: int = 0

    height: int = 0

    confidence: float = 0.0

    text: str = ""

    boxes: List[OCRBox] | None = None

    def center(self):
        """
        返回目标中心坐标
        """

        return (
            self.x + self.width // 2,
            self.y + self.height // 2
        )