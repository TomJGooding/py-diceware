from dataclasses import dataclass

from wordlist import WordList


@dataclass
class PassphraseDefaults:
    number_of_words: int
    min_words: int
    delimiter: str
    capitalisation: bool
    wordlist: WordList


PASSPHRASE_DEFAULTS = PassphraseDefaults(
    number_of_words=6,
    min_words=1,
    delimiter="",
    capitalisation=True,
    wordlist=WordList("diceware.wordlist.asc"),
)
