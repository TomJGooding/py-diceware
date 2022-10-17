from dataclasses import dataclass
from pathlib import Path

WORDLISTS_PATH = Path("./wordlists/")


@dataclass
class WordList:
    filename: str
    path: Path = WORDLISTS_PATH
