from dataclasses import dataclass


@dataclass(slots=True)
class Target:
    """
    一次识别结果
    """

    name: str

    x: int

    y: int

    score: float