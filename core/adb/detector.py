from core.adb.adapter import ADBAdapter
from core.adb.models import DeviceInfo


class DeviceDetector:

    def __init__(self):

        self.adapter = ADBAdapter()

    def scan(self):

        result = []

        for adb_device in self.adapter.list_devices():

            serial = adb_device.serial

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
                    adb_device=adb_device,
                    serial=serial,
                    emulator=emulator,
                    score=score,
                )
            )

        result.sort(
            key=lambda d: d.score,
            reverse=True,
        )

        return result