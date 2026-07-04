from core.adb.manager import DeviceManager
from core.logger.logger import logger


def main():

    logger.info("WWA Start")

    manager = DeviceManager()

    device = manager.connect()

    logger.info(
        f"当前设备：{device.serial}"
    )

    device.screenshot(
        "resources/screenshots/test.png"
    )


if __name__ == "__main__":

    main()