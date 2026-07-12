"""
OCR识别模块

使用：

RapidOCR

特点：

速度快

中文识别效果好

适合自动化项目
"""

from typing import List

from rapidocr_onnxruntime import RapidOCR

from .result import OCRBox


class OCR:

    """
    OCR识别器
    """

    def __init__(self):

        self.engine = RapidOCR()

    def recognize(
        self,
        image
    ) -> List[OCRBox]:
        """
        OCR识别

        Returns
        -------
        List[OCRBox]
        """

        result, _ = self.engine(image)

        boxes = []

        if result is None:

            return boxes

        for item in result:

            points = item[0]

            text = item[1]

            score = float(item[2])

            xs = [p[0] for p in points]
            ys = [p[1] for p in points]

            x = int(min(xs))
            y = int(min(ys))

            w = int(max(xs) - min(xs))
            h = int(max(ys) - min(ys))

            boxes.append(

                OCRBox(

                    text=text,

                    confidence=score,

                    x=x,

                    y=y,

                    width=w,

                    height=h

                )

            )

        return boxes