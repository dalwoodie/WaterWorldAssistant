from dataclasses import dataclass


@dataclass(slots=True)
class DeviceInfo:
    """
    设备信息
    """

    adb_device: object

    serial: str

    emulator: str

    score: int