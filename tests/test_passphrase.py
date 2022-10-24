import pytest

from py_diceware.config import PassphraseDefaults
from py_diceware.passphrase import Passphrase
from py_diceware.roll_dice import roll_dice


def test_passphrase_lookup_words():
    dice_rolls = roll_dice(num_rolls=6, num_dice=5, sides=1)
    passphrase = Passphrase(
        PassphraseDefaults.number_of_words,
        PassphraseDefaults.delimiter,
        PassphraseDefaults.capitalisation,
        dice_rolls,
        PassphraseDefaults.wordlist,
    )
    assert passphrase.words == ["a", "a", "a", "a", "a", "a"]
    assert len(passphrase.words) == 6


def test_passphrase_lookup_words_with_set_dice():
    dice_rolls = roll_dice(num_rolls=6)
    passphrase = Passphrase(
        PassphraseDefaults.number_of_words,
        PassphraseDefaults.delimiter,
        PassphraseDefaults.capitalisation,
        dice_rolls,
        PassphraseDefaults.wordlist,
    )

    passphrase.dice_rolls = [16665, 15653, 56322, 35616, 65224, 64326]
    correct_words = ["cleft", "cam", "synod", "lacy", "yr", "wok"]
    assert len(passphrase.words) == 6
    for idx, dice in enumerate(passphrase.dice_rolls):
        assert passphrase.lookup_word(dice) == correct_words[idx]


def test_passphrase_lookup_words_lookup_error():
    dice_rolls = roll_dice(num_rolls=1)
    passphrase = Passphrase(
        PassphraseDefaults.number_of_words,
        PassphraseDefaults.delimiter,
        PassphraseDefaults.capitalisation,
        dice_rolls,
        PassphraseDefaults.wordlist,
    )

    passphrase.dice_rolls = ["This does not appear in the wordlist!"]
    with pytest.raises(LookupError):
        for dice in passphrase.dice_rolls:
            passphrase.lookup_word(dice)


def test_passphrase_generate_passphrase_with_defaults():
    dice_rolls = roll_dice(num_rolls=6, num_dice=5, sides=1)
    passphrase = Passphrase(
        PassphraseDefaults.number_of_words,
        PassphraseDefaults.delimiter,
        PassphraseDefaults.capitalisation,
        dice_rolls,
        PassphraseDefaults.wordlist,
    )
    assert passphrase.generate_passphrase() == "AAAAAA"


def test_passphrase_generate_passphrase_with_delimiter():
    delimiter = "_"
    dice_rolls = roll_dice(num_rolls=6, num_dice=5, sides=1)
    passphrase = Passphrase(
        PassphraseDefaults.number_of_words,
        delimiter,
        PassphraseDefaults.capitalisation,
        dice_rolls,
        PassphraseDefaults.wordlist,
    )
    assert passphrase.generate_passphrase() == "A_A_A_A_A_A"


def test_passphrase_generate_passphrase_no_capitalisation():
    capitalisation = False
    dice_rolls = roll_dice(num_rolls=6, num_dice=5, sides=1)
    passphrase = Passphrase(
        PassphraseDefaults.number_of_words,
        PassphraseDefaults.delimiter,
        capitalisation,
        dice_rolls,
        PassphraseDefaults.wordlist,
    )
    assert passphrase.generate_passphrase() == "aaaaaa"
