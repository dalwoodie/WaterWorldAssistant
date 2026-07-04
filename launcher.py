from game.context import GameContext


def main():

    ctx = GameContext()

    device = ctx.connect_device()

    ctx.logger.info(
        f"当前设备：{device.serial}"
    )

    device.screenshot(
        "resources/screenshots/test.png"
    )

    ctx.logger.info("截图完成")


if __name__ == "__main__":

    main()