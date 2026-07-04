from .base import BaseScene


class WorldScene(BaseScene):

    name = "World"

    def check(self) -> bool:
        return False