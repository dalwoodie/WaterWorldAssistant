from abc import ABC, abstractmethod


class BaseScene(ABC):

    name = "Unknown"

    def __init__(self, context):

        self.context = context

    @abstractmethod
    def check(self) -> bool:
        """
        判断当前是否属于该场景
        """
        pass