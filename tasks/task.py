"""
任务基类

所有自动化任务都继承 Task。

例如：

AttackTask

CollectTask

RepairTask
"""

from abc import ABC, abstractmethod


class Task(ABC):

    def __init__(self):

        self.finished = False

    @property
    @abstractmethod
    def name(self):
        """
        任务名称
        """
        pass

    @abstractmethod
    def run(self):
        """
        执行任务
        """
        pass