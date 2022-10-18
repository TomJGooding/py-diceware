import pytest
from pytest import MonkeyPatch

from diceware import (
    PASSPHRASE_DEFAULTS,
    Passphrase,
    is_valid_int,
    is_valid_y_or_n,
    read_capitalisation,
    read_delimiter,
    read_number_of_words,
)
from roll_dice import roll_dice


def test_is_valid_int_when_input_is_valid():
    valid_input = "6"
    result = is_valid_int(valid_input, min_value=6)
    assert result is True


def test_is_valid_int_when_input_is_not_a_number(capfd):
    invalid_input = "This is not a number!"
    result = is_valid_int(invalid_input, min_value=3)
    out, _ = capfd.readouterr()
    assert result is False
    assert "Please enter a number." in out


def test_is_valid_int_when_input_is_too_low(capfd):
    invalid_input = "1"
    result = is_valid_int(invalid_input, min_value=3)
    out, _ = capfd.readouterr()
    assert result is False
    assert "The minimum value is 3" in out


def test_read_number_of_words_valid_input(monkeypatch: MonkeyPatch):
    valid_input = "7"
    monkeypatch.setattr("builtins.input", lambda _: valid_input)
    result = read_number_of_words("Number of words: ")
    assert result == 7


def test_read_number_of_words_empty_input_defaults(monkeypatch: MonkeyPatch):
    empty_input = ""
    monkeypatch.setattr("builtins.input", lambda _: empty_input)
    result = read_number_of_words("Number of words: ")
    assert result == 6


def test_read_delimiter_with_input(monkeypatch: MonkeyPatch):
    input = "_"
    monkeypatch.setattr("builtins.input", lambda _: input)
    result = read_delimiter("Delimiter: ")
    assert result == "_"


def test_is_valid_y_or_n_with_valid_input():
    input = "Yes"
    result = is_valid_y_or_n(input)
    assert result is True


def test_is_valid_y_or_n_with_invalid_input(capfd):
    input = "This string is not [y]es or [n]o!"
    result = is_valid_y_or_n(input)
    out, _ = capfd.readouterr()
    assert result is False
    assert "Please answer yes or no." in out


def test_read_capitalisation_with_y_input(monkeypatch: MonkeyPatch):
    input = "yEs"
    monkeypatch.setattr("builtins.input", lambda _: input)
    result = read_capitalisation("Capitalisation? [Y/n] ")
    assert result is True


def test_read_capitalisation_with_n_input(monkeypatch: MonkeyPatch):
    input = "nO"
    monkeypatch.setattr("builtins.input", lambda _: input)
    result = read_capitalisation("Capitalisation? [Y/n] ")
    assert result is False


def test_read_capitalisation_empty_input_defaults(monkeypatch: MonkeyPatch):
    input = ""
    monkeypatch.setattr("builtins.input", lambda _: input)
    result = read_capitalisation("Capitalisation? [Y/n] ")
    assert result is True


def test_passphrase_lookup_words():
    dice_rolls = roll_dice(num_rolls=6, num_dice=5, sides=1)
    passphrase = Passphrase(
        PASSPHRASE_DEFAULTS.number_of_words,
        PASSPHRASE_DEFAULTS.delimiter,
        PASSPHRASE_DEFAULTS.capitalisation,
        dice_rolls,
        PASSPHRASE_DEFAULTS.wordlist,
    )
    assert passphrase.words == ["a", "a", "a", "a", "a", "a"]
    assert len(passphrase.words) == 6


def test_passphrase_lookup_words_with_set_dice():
    dice_rolls = roll_dice(num_rolls=6)
    passphrase = Passphrase(
        PASSPHRASE_DEFAULTS.number_of_words,
        PASSPHRASE_DEFAULTS.delimiter,
        PASSPHRASE_DEFAULTS.capitalisation,
        dice_rolls,
        PASSPHRASE_DEFAULTS.wordlist,
    )

    passphrase.dice_rolls = [16665, 15653, 56322, 35616, 65224, 64326]
    correct_words = ["cleft", "cam", "synod", "lacy", "yr", "wok"]
    assert len(passphrase.words) == 6
    for idx, dice in enumerate(passphrase.dice_rolls):
        assert passphrase.lookup_word(dice) == correct_words[idx]


def test_passphrase_lookup_words_lookup_error():
    dice_rolls = roll_dice(num_rolls=1)
    passphrase = Passphrase(
        PASSPHRASE_DEFAULTS.number_of_words,
        PASSPHRASE_DEFAULTS.delimiter,
        PASSPHRASE_DEFAULTS.capitalisation,
        dice_rolls,
        PASSPHRASE_DEFAULTS.wordlist,
    )

    passphrase.dice_rolls = ["This does not appear in the wordlist!"]
    with pytest.raises(LookupError):
        for dice in passphrase.dice_rolls:
            passphrase.lookup_word(dice)


def test_passphrase_generate_passphrase_with_defaults():
    dice_rolls = roll_dice(num_rolls=6, num_dice=5, sides=1)
    passphrase = Passphrase(
        PASSPHRASE_DEFAULTS.number_of_words,
        PASSPHRASE_DEFAULTS.delimiter,
        PASSPHRASE_DEFAULTS.capitalisation,
        dice_rolls,
        PASSPHRASE_DEFAULTS.wordlist,
    )
    assert passphrase.generate_passphrase() == "AAAAAA"


def test_passphrase_generate_passphrase_with_delimiter():
    delimiter = "_"
    dice_rolls = roll_dice(num_rolls=6, num_dice=5, sides=1)
    passphrase = Passphrase(
        PASSPHRASE_DEFAULTS.number_of_words,
        delimiter,
        PASSPHRASE_DEFAULTS.capitalisation,
        dice_rolls,
        PASSPHRASE_DEFAULTS.wordlist,
    )
    assert passphrase.generate_passphrase() == "A_A_A_A_A_A"


def test_passphrase_generate_passphrase_no_capitalisation():
    capitalisation = False
    dice_rolls = roll_dice(num_rolls=6, num_dice=5, sides=1)
    passphrase = Passphrase(
        PASSPHRASE_DEFAULTS.number_of_words,
        PASSPHRASE_DEFAULTS.delimiter,
        capitalisation,
        dice_rolls,
        PASSPHRASE_DEFAULTS.wordlist,
    )
    assert passphrase.generate_passphrase() == "aaaaaa"
