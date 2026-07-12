from dataclasses import dataclass


@dataclass
class ADBDevice:

    serial: str

    status: str = "device"

    model: str = ""

    android_version: str = ""

    width: int = 0

    height: int = 0

    def __str__(self):

        if self.model:

            return f"{self.model} ({self.serial})"

        return self.serial