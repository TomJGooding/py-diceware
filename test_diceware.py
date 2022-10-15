from pytest import MonkeyPatch

from diceware import is_valid_int, read_delimiter, read_int


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


def test_read_int_valid_input(monkeypatch: MonkeyPatch):
    valid_input = "6"
    monkeypatch.setattr("builtins.input", lambda _: valid_input)
    result = read_int("Enter a number: ")
    assert result == 6


def test_read_delimiter(monkeypatch: MonkeyPatch):
    input = "_"
    monkeypatch.setattr("builtins.input", lambda _: input)
    result = read_delimiter("Delimiter: ")
    assert result == "_"
