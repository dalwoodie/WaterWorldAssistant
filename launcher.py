from game.context import GameContext


def main():

    ctx = GameContext()

    device = ctx.connect_device()

    ctx.logger.info(
        f"当前设备：{device.serial}"
    )

    device.screenshot(
        ctx.resource.screenshot("test")
    )

    ctx.logger.info("截图完成")

    ctx.task_manager.run()

    scene = ctx.scene.detect()

    ctx.logger.info(f"当前Scene：{scene.name}")


if __name__ == "__main__":
    main()