import cv2
import numpy as np


class Screenshot:

    @staticmethod
    def capture(manager, device):

        result = manager.adb_command(

            [

                "-s",

                device.serial,

                "exec-out",

                "screencap",

                "-p"

            ]

        )

        image = np.frombuffer(

            result.stdout.encode("latin1"),

            np.uint8

        )

        img = cv2.imdecode(

            image,

            cv2.IMREAD_COLOR

        )

        if img is None:

            raise RuntimeError(

                "截图失败。"

            )

        return img