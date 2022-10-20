from pytest import MonkeyPatch

from py_diceware.cli import (
    is_valid_int,
    is_valid_y_or_n,
    read_capitalisation,
    read_delimiter,
    read_number_of_words,
)


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
