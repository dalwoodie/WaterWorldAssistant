from abc import ABC


class BaseScene(ABC):
    """场景基类"""

    # 场景名称
    name = "Unknown"

    # 当前场景的识别模板
    anchors = []

    def __init__(self, context):
        """
        初始化场景
        """
        self.context = context

    def check(self, screenshot):
        """
        判断当前截图是否属于本场景
        """
        return self.context.vision.exists_all(
            screenshot,
            self.anchors
        )