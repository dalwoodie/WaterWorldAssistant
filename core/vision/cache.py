"""
Vision缓存

用于缓存：

最近截图

模板

OCR结果

减少重复识别。
"""


class VisionCache:

    def __init__(self):

        self.last_image = None

        self.last_result = None

        self.templates = {}

    def clear(self):
        """
        清空缓存
        """

        self.last_image = None

        self.last_result = None

        self.templates.clear()