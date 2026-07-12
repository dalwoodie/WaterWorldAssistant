"""
ADB管理器
"""

from pathlib import Path
import subprocess
import yaml

from .adb_device import ADBDevice


class ADBManager:

    def __init__(self):

        self.devices = []

        self.adb = self.load_adb_path()

    def load_adb_path(self):

        """
        获取adb路径

        优先级：

        config.yaml

        ↓

        系统PATH
        """

        config = Path("config/config.yaml")

        if config.exists():

            with open(
                config,
                "r",
                encoding="utf-8"
            ) as f:

                data = yaml.safe_load(f)

                adb = data.get("adb", {}).get(
                    "executable",
                    ""
                )

                if adb:

                    return adb

        return "adb"

    def adb_command(self, args):

        """
        执行adb命令
        """

        cmd = [self.adb]

        cmd.extend(args)

        try:

            result = subprocess.run(

                cmd,

                capture_output=True,

                text=True,

                timeout=10

            )

            return result

        except FileNotFoundError:

            raise RuntimeError(

                "\n未找到 adb.exe\n\n"

                "请执行以下任意一种：\n"

                "① config/config.yaml 设置 adb.executable\n"

                "② 将 adb 加入 PATH\n"

                "③ tools/adb/ 放置 adb.exe"

            )

    def refresh(self):

        """
        刷新设备
        """

        self.devices.clear()

        result = self.adb_command(

            ["devices"]

        )

        lines = result.stdout.splitlines()

        if len(lines) <= 1:

            return []

        for line in lines[1:]:

            if not line.strip():

                continue

            parts = line.split()

            if len(parts) < 2:

                continue

            self.devices.append(

                ADBDevice(

                    serial=parts[0],

                    status=parts[1]

                )

            )

        return self.devices

    def get_default_device(self):

        if not self.devices:

            self.refresh()

        if not self.devices:

            return None

        return self.devices[0]