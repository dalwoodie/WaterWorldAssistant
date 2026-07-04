"""
ADBAdapter

整个项目唯一允许直接调用 adbutils 的地方。
"""

from adbutils import adb


class ADBAdapter:

    def list_devices(self):
        """返回 adbutils Device 列表"""
        return adb.device_list()