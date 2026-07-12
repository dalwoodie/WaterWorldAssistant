"""
图像处理工具

统一提供：

灰度

裁剪

缩放

二值化

OCR增强
"""

import cv2


class ImageUtil:

    @staticmethod
    def gray(image):
        """
        转灰度
        """

        return cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

    @staticmethod
    def resize(image, scale):
        """
        缩放
        """

        return cv2.resize(
            image,
            None,
            fx=scale,
            fy=scale
        )

    @staticmethod
    def crop(
        image,
        x,
        y,
        w,
        h
    ):
        """
        裁剪区域
        """

        return image[
            y:y + h,
            x:x + w
        ]

    @staticmethod
    def binary(
        image,
        threshold=180
    ):
        """
        固定阈值二值化
        """

        gray = ImageUtil.gray(image)

        _, binary = cv2.threshold(
            gray,
            threshold,
            255,
            cv2.THRESH_BINARY
        )

        return binary

    @staticmethod
    def adaptive_binary(image):
        """
        自适应二值化
        """

        gray = ImageUtil.gray(image)

        return cv2.adaptiveThreshold(
            gray,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11,
            2
        )

    @staticmethod
    def enhance_text(image):
        """
        OCR文字增强
        """

        return ImageUtil.adaptive_binary(image)