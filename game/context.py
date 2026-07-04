from core.adb.manager import DeviceManager
from core.config.manager import ConfigManager
from core.logger.logger import logger


class GameContext:

    def __init__(self):

        logger.info("初始化 GameContext")

        self.logger = logger

        self.config = ConfigManager()

        self.device_manager = DeviceManager()

        self.device = None

    def connect_device(self):

        self.device = self.device_manager.connect()

        return self.device