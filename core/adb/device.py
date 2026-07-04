from pathlib import Path


class Device:

    def __init__(self, adb_device):

        self._device = adb_device

    @property
    def serial(self):

        return self._device.serial

    def tap(self, x, y):

        self._device.shell(
            f"input tap {x} {y}"
        )

    def screenshot(self, save_path):

        save_path = Path(save_path)

        save_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        image = self._device.screenshot()

        image.save(save_path)