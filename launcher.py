from core.logger.logger import logger
from core.config.manager import ConfigManager


def main():

    logger.info("WaterWorldAssistant Start")

    config = ConfigManager()

    logger.info(
        f"Game Resolution: "
        f'{config.get("game","width")}x'
        f'{config.get("game","height")}'
    )


if __name__ == "__main__":

    main()