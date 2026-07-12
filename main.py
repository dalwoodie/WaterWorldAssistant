from core.adb import ADBManager
from core.logger import Logger

from features.city import CityFeature
from features.fleet import FleetFeature
from features.ship import ShipFeature
from features.resource import ResourceFeature


def main():

    logger = Logger.get()

    logger.info("=" * 50)
    logger.info("Water World Assistant")
    logger.info("Commit11")
    logger.info("=" * 50)

    adb = ADBManager()

    try:

        devices = adb.refresh()

    except Exception as e:

        logger.error(str(e))

        return

    if not devices:

        logger.error("未发现ADB设备。")

        return

    logger.info(

        f"当前设备：{devices[0]}"

    )

    features = [

        CityFeature(),

        FleetFeature(),

        ShipFeature(),

        ResourceFeature()

    ]

    logger.info(

        "初始化完成。"

    )


if __name__ == "__main__":

    main()