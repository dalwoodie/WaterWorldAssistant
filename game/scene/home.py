from .base import BaseScene


class HomeScene(BaseScene):

    name = "Home"

    def check(self) -> bool:
        """
        Commit7开始实现模板识别
        """
        return False