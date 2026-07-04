from pathlib import Path

import cv2
import numpy as np
from PIL import Image

from core.vision.target import Target


class TemplateMatcher:

    def find(
        self,
        screenshot: Image.Image,
        template_path: Path,
        threshold: float = 0.8,
        name: str = "unknown",
    ) -> Target | None:
        """
        模板匹配
        """

        screenshot = cv2.cvtColor(
            np.array(screenshot),
            cv2.COLOR_RGB2BGR,
        )

        template = cv2.imread(
            str(template_path),
            cv2.IMREAD_COLOR,
        )

        if template is None:
            raise FileNotFoundError(template_path)

        result = cv2.matchTemplate(
            screenshot,
            template,
            cv2.TM_CCOEFF_NORMED,
        )

        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val < threshold:
            return None

        h, w = template.shape[:2]

        return Target(
            name=name,
            x=max_loc[0] + w // 2,
            y=max_loc[1] + h // 2,
            score=float(max_val),
        )