"""
Vision统一识别入口

整个项目以后只允许 Feature 调用 VisionEngine。

VisionEngine 负责：

1. 模板匹配
2. OCR识别
3. 图像裁剪
4. 判断目标是否存在

Feature 不允许直接调用：

OpenCV
PaddleOCR
TemplateMatcher
"""

from typing import List, Optional

from .image import ImageUtil
from .matcher import TemplateMatcher
from .ocr import OCR
from .region import Region
from .result import OCRBox, VisionResult
from .template import TemplateManager


class VisionEngine:
    """
    Vision统一识别引擎
    """

    def __init__(self):

        self.template_manager = TemplateManager()

        self.ocr = OCR()

    # ==========================================================
    # 图像处理
    # ==========================================================

    def crop(
        self,
        image,
        region: Region
    ):
        """
        裁剪指定区域
        """

        return ImageUtil.crop(
            image,
            region.x,
            region.y,
            region.width,
            region.height
        )

    # ==========================================================
    # Template
    # ==========================================================

    def find_template(
        self,
        image,
        template_name: str,
        threshold: float = 0.85
    ) -> VisionResult:
        """
        查找单个模板
        """

        template = self.template_manager.load(
            template_name
        )

        return TemplateMatcher.match(
            image,
            template,
            threshold
        )

    def find_templates(
        self,
        image,
        template_name: str,
        threshold: float = 0.85
    ) -> List[VisionResult]:
        """
        查找所有模板
        """

        template = self.template_manager.load(
            template_name
        )

        return TemplateMatcher.match_all(
            image,
            template,
            threshold
        )

    def exists(
        self,
        image,
        template_name: str,
        threshold: float = 0.85
    ) -> bool:
        """
        判断模板是否存在
        """

        result = self.find_template(
            image,
            template_name,
            threshold
        )

        return result.found

    # ==========================================================
    # OCR
    # ==========================================================

    def recognize(
        self,
        image
    ) -> List[OCRBox]:
        """
        OCR识别全部文字
        """

        return self.ocr.recognize(
            image
        )

    def find_text(
        self,
        image,
        keyword: str,
        region: Optional[Region] = None
    ) -> VisionResult:
        """
        查找指定文字

        Parameters
        ----------
        keyword
            要查找的文本

        region
            OCR区域，可为空

        Returns
        -------
        VisionResult
        """

        if region is not None:

            image = self.crop(
                image,
                region
            )

            offset_x = region.x
            offset_y = region.y

        else:

            offset_x = 0
            offset_y = 0

        boxes = self.recognize(
            image
        )

        for box in boxes:

            if keyword in box.text:

                return VisionResult(

                    found=True,

                    x=box.x + offset_x,

                    y=box.y + offset_y,

                    width=box.width,

                    height=box.height,

                    confidence=box.confidence,

                    text=box.text,

                    boxes=boxes

                )

        return VisionResult(

            found=False,

            boxes=boxes

        )

    def recognize_region(
        self,
        image,
        region: Region
    ) -> List[OCRBox]:
        """
        OCR识别指定区域全部文字
        """

        crop = self.crop(
            image,
            region
        )

        boxes = self.recognize(
            crop
        )

        for box in boxes:

            box.x += region.x
            box.y += region.y

        return boxes