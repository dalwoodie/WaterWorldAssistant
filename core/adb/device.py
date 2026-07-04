"""
设备对象

负责：
- 点击
- 滑动
- 截图
"""

from pathlib import Path


class Device:

    def __init__(self, adb_device):

        self._device = adb_device

    @property
    def serial(self):

        return self._device.serial

    def tap(self, x: int, y: int):

        self._device.shell(
            f"input tap {x} {y}"
        )

    def swipe(
        self,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        duration: int = 300
    ):

        self._device.shell(
            f"input swipe {x1} {y1} {x2} {y2} {duration}"
        )

    def screenshot(self, path):

        img = self._device.screenshot()

        Path(path).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        img.save(path)