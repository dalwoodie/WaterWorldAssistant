import time

from core.vision.matcher import TemplateMatcher
from core.vision.result import MatchResult


class VisionService:

    def __init__(self, context):

        self.context = context

        self.matcher = TemplateMatcher()

    def find(self, screenshot, template, threshold=0.8):

        result = self.matcher.match(
            screenshot,
            template,
            threshold
        )

        if result is None:

            return MatchResult()

        return MatchResult(
            found=True,
            confidence=result.confidence,
            x=result.x,
            y=result.y,
            width=result.width,
            height=result.height
        )

    def exists(self, screenshot, template, threshold=0.8):

        return self.find(
            screenshot,
            template,
            threshold
        ).found

    def wait(
            self,
            screenshot_getter,
            template,
            timeout=10,
            interval=0.5,
            threshold=0.8
    ):

        start = time.time()

        while time.time() - start < timeout:

            screenshot = screenshot_getter()

            result = self.find(
                screenshot,
                template,
                threshold
            )

            if result.found:

                return result

            time.sleep(interval)

        return MatchResult()