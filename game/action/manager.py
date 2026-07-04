import time


class ActionManager:

    def __init__(self, context):

        self.context = context

    def click(self, x: int, y: int):

        self.context.device.click(x, y)

    def click_center(self, result):

        x, y = result.center

        self.click(x, y)

    def click_if_exists(
            self,
            screenshot,
            template,
            threshold=0.8
    ):

        result = self.context.vision.find(
            screenshot,
            template,
            threshold
        )

        if not result.found:

            return False

        self.click_center(result)

        return True

    def wait(
            self,
            screenshot_getter,
            template,
            timeout=10,
            interval=0.5
    ):

        return self.context.vision.wait(
            screenshot_getter,
            template,
            timeout,
            interval
        )

    def sleep(self, seconds):

        time.sleep(seconds)