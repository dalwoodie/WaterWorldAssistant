"""
OCR区域定义

所有坐标均基于：

MuMu模拟器

1280 × 720
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Region:
    """
    图像区域
    """

    x: int

    y: int

    width: int

    height: int


class Regions:
    """
    常用识别区域

    后续随着功能开发不断补充。
    """

    # 左侧城市快捷栏
    CITY_LIST = Region(
        0,
        80,
        220,
        560
    )

    # 左下舰队状态
    FLEET_STATUS = Region(
        0,
        500,
        350,
        220
    )

    # 货轮列表
    SHIP_LIST = Region(
        760,
        120,
        500,
        520
    )

    # 顶部资源栏
    RESOURCE_BAR = Region(
        260,
        0,
        760,
        70
    )