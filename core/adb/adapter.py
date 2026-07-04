"""
ADBAdapter

整个WWA唯一允许直接调用 adbutils 的地方。
"""

from adbutils import adb


class ADBAdapter:

    def list_devices(self):
        """
        返回 adbutils 的 Device 对象列表
        """
        return adb.device_list()

    def get_device(self, serial: str):
        """
        根据 serial 获取 Device
        """
        return adb.device(serial)