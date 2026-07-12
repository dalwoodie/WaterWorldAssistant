"""
战斗模块

负责：

攻击

集结

防守

Commit12以后实现。
"""

from features.base import BaseFeature


class BattleFeature(BaseFeature):

    @property
    def name(self):

        return "Battle"

    def run(self):

        self.log("Battle Feature Running...")