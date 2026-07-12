"""
城市模块

负责：

城市识别

城市切换

城市状态读取

Commit11开始实现OCR识别。
"""

from features.base import BaseFeature


class CityFeature(BaseFeature):

    @property
    def name(self):

        return "City"

    def run(self):

        self.log("City Feature Running...")