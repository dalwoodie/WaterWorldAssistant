"""
模板匹配模块

负责：

1. 单目标匹配
2. 多目标匹配

整个项目禁止直接调用
cv2.matchTemplate()

统一通过 TemplateMatcher。
"""

from typing import List

import cv2
import numpy as np

from .result import VisionResult


class TemplateMatcher:
    """
    OpenCV模板匹配
    """

    @staticmethod
    def match(
        screenshot,
        template,
        threshold: float = 0.85
    ) -> VisionResult:
        """
        单目标匹配

        Returns
        -------
        VisionResult
        """

        result = cv2.matchTemplate(
            screenshot,
            template,
            cv2.TM_CCOEFF_NORMED
        )

        _, confidence, _, location = cv2.minMaxLoc(result)

        if confidence < threshold:
            return VisionResult(False)

        h, w = template.shape[:2]

        return VisionResult(
            found=True,
            x=location[0],
            y=location[1],
            width=w,
            height=h,
            confidence=float(confidence)
        )

    @staticmethod
    def match_all(
        screenshot,
        template,
        threshold: float = 0.85,
        distance: int = 10
    ) -> List[VisionResult]:
        """
        多目标匹配

        Parameters
        ----------
        distance
            去重距离（像素）

        Returns
        -------
        List[VisionResult]
        """

        result = cv2.matchTemplate(
            screenshot,
            template,
            cv2.TM_CCOEFF_NORMED
        )

        locations = np.where(result >= threshold)

        h, w = template.shape[:2]

        matches: List[VisionResult] = []

        for y, x in zip(*locations):

            duplicated = False

            for item in matches:

                if (
                    abs(item.x - x) < distance
                    and
                    abs(item.y - y) < distance
                ):
                    duplicated = True
                    break

            if duplicated:
                continue

            matches.append(

                VisionResult(

                    found=True,

                    x=int(x),

                    y=int(y),

                    width=w,

                    height=h,

                    confidence=float(
                        result[y][x]
                    )

                )

            )

        matches.sort(

            key=lambda item: item.confidence,

            reverse=True

        )

        return matches