from .base import BaseScene


class UnknownScene(BaseScene):

    name = "Unknown"

    def check(self, screenshot):
        return True