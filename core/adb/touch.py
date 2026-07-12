class Touch:

    @staticmethod
    def click(

        manager,

        device,

        x,

        y

    ):

        manager.adb_command(

            [

                "-s",

                device.serial,

                "shell",

                "input",

                "tap",

                str(x),

                str(y)

            ]

        )

        return True

    @staticmethod
    def swipe(

        manager,

        device,

        x1,

        y1,

        x2,

        y2,

        duration=300

    ):

        manager.adb_command(

            [

                "-s",

                device.serial,

                "shell",

                "input",

                "swipe",

                str(x1),

                str(y1),

                str(x2),

                str(y2),

                str(duration)

            ]

        )

        return True