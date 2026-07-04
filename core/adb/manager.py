"""
ADB设备管理
"""

from adbutils import adb

from core.adb.device import Device
from core.logger.logger import logger


class DeviceManager:

    def list_devices(self):

        return adb.device_list()

    def connect(self, serial=None):

        devices = self.list_devices()

        if len(devices) == 0:

            raise RuntimeError("没有发现ADB设备")

        logger.info("发现设备：")

        for i, d in enumerate(devices):

            logger.info(f"[{i}] {d.serial}")

        #
        # 自动连接
        #

        if serial is None:

            device = devices[0]

        else:

            device = next(
                d
                for d in devices
                if d.serial == serial
            )

        logger.info(
            f"连接设备：{device.serial}"
        )

        return Device(device)