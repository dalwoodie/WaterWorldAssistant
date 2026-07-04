from adbutils import adb

from core.adb.device import Device
from core.logger.logger import logger


class DeviceManager:

    def list_devices(self):

        return adb.device_list()

    def connect(self):

        devices = self.list_devices()

        if not devices:

            raise RuntimeError("没有找到ADB设备")

        logger.info("检测到ADB设备：")

        for index, device in enumerate(devices):

            logger.info(
                f"[{index}] {device.serial}"
            )

        #
        # 第一版默认连接第一个设备
        #

        adb_device = devices[0]

        logger.info(
            f"连接设备：{adb_device.serial}"
        )

        return Device(adb_device)