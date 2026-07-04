from pathlib import Path


class ResourceManager:
    """
    管理项目资源路径
    """

    def __init__(self):

        self.root = Path("resources")

    @property
    def templates(self):

        return self.root / "templates"

    @property
    def screenshots(self):

        return self.root / "screenshots"

    @property
    def icons(self):

        return self.root / "icons"

    def template(self, name: str):

        """
        获取模板路径
        """

        return self.templates / f"{name}.png"

    def screenshot(self, name: str):

        return self.screenshots / f"{name}.png"