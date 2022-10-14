import pytest
from pytest import MonkeyPatch

from diceware import read_int


def test_read_int_valid_number(monkeypatch: MonkeyPatch):
    input = "6"
    monkeypatch.setattr("builtins.input", lambda _: input)
    number = read_int("Enter a number more than 5: ", min_value=5)
    assert number == 6


def test_read_int_not_a_number(monkeypatch: MonkeyPatch):
    # TODO
    pass


def test_read_int_number_too_low(monkeypatch: MonkeyPatch):
    # TODO
    pass
