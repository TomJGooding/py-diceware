import secrets
from typing import Optional

"""Python's random module generates only pseudo-random numbers
and is designed for modelling and simulation, not security or cryptography.

The secrets module is used for generating cryptographically strong random
numbers suitable for managing data such as passphrases.

See PEP 506 (https://peps.python.org/pep-0506/)
"""


class Die:
    def __init__(self, face: Optional[int] = None, sides: int = 6) -> None:
        self.sides: int = sides
        if face is not None:
            self.face: int = face
        else:
            self.roll()

    def roll(self) -> int:
        self.face = secrets.randbelow(self.sides) + 1
        return self.face

    def __str__(self) -> str:
        return str(self.face)


class Dice:
    def __init__(self, num_dice: int = 5, sides: int = 6) -> None:
        self.num_dice: int = num_dice
        self.dice: list[Die] = []
        for _ in range(num_dice):
            self.dice.append(Die(sides=sides))

    def __str__(self) -> str:
        return "".join([f"{die}" for die in self.dice])
