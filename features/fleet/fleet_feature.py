"""
舰队模块

负责：

舰队状态

舰队数量

舰队调度
"""

from features.base import BaseFeature


class FleetFeature(BaseFeature):

    @property
    def name(self):

        return "Fleet"

    def run(self):

        self.log("Fleet Feature Running...")