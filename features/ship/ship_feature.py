"""
货轮模块

负责：

货轮识别

货轮筛选

货轮点击
"""

from features.base import BaseFeature


class ShipFeature(BaseFeature):

    @property
    def name(self):

        return "Ship"

    def run(self):

        self.log("Ship Feature Running...")