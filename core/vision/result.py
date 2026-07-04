from dataclasses import dataclass


@dataclass
class MatchResult:
    found: bool = False

    confidence: float = 0.0

    x: int = 0
    y: int = 0

    width: int = 0
    height: int = 0

    @property
    def center(self):

        return (
            self.x + self.width // 2,
            self.y + self.height // 2
        )