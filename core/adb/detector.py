from adbutils import adb

from core.adb.models import DeviceInfo


class DeviceDetector:
    """
    扫描并排序ADB设备
    """

    def scan(self) -> list[DeviceInfo]:
        result = []

        for device in adb.device_list():

            serial = device.serial

            emulator = "Unknown"

            score = 10

            if serial.startswith("127.0.0.1:16384"):
                emulator = "MuMu"
                score = 100

            elif serial.startswith("127.0.0.1:7555"):
                emulator = "MuMu"
                score = 90

            elif serial.startswith("emulator-"):
                emulator = "Android Emulator"
                score = 60

            result.append(
                DeviceInfo(
                    serial=serial,
                    emulator=emulator,
                    score=score,
                )
            )

        result.sort(
            key=lambda x: x.score,
            reverse=True,
        )

        return result