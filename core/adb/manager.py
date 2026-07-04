from core.adb.adapter import ADBAdapter

from core.adb.detector import DeviceDetector
from core.adb.device import Device
from core.logger.logger import logger


class DeviceManager:

    def __init__(self):

        self.adapter = ADBAdapter()

    def connect(self):

        devices = self.detector.scan()

        if not devices:
            raise RuntimeError("没有发现ADB设备")

        logger.info("检测到ADB设备：")

        for index, device in enumerate(devices):

            logger.info(
                f"[{index}] "
                f"{device.serial} "
                f"({device.emulator}) "
                f"score={device.score}"
            )

        best = devices[0]

        logger.info(
            f"自动选择：{best.serial}"
        )

        adb_device = self.adapter.get_device(best.serial)

        return Device(adb_device)