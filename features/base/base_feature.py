"""
所有功能模块基类

例如：

CityFeature
FleetFeature
ShipFeature

都继承 BaseFeature。
"""

from abc import ABC, abstractmethod

from core.logger import Logger


class BaseFeature(ABC):
    """
    功能模块基类
    """

    def __init__(self):

        self.logger = Logger.get()

        self.enabled = True

    @property
    @abstractmethod
    def name(self) -> str:
        """
        功能名称
        """
        pass

    def enable(self):
        """
        启用功能
        """

        self.enabled = True

    def disable(self):
        """
        禁用功能
        """

        self.enabled = False

    def is_enabled(self) -> bool:
        """
        是否启用
        """

        return self.enabled

    def log(self, message: str):
        """
        输出日志
        """

        self.logger.info(
            f"[{self.name}] {message}"
        )

    @abstractmethod
    def run(self):
        """
        功能入口
        """
        pass