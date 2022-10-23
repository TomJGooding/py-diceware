from click.testing import CliRunner

from py_diceware.cli import main

"""These cli tests rely on:
    - the passphrase being the final line in the output
    - the diceware word list not containing any underscores
"""

PASSPHRASE_OUTPUT_LINE: int = -1


def test_cli_passphrase_delimiter():
    runner = CliRunner()
    result = runner.invoke(main, "--delimiter '_'")
    passphrase_output = result.output.splitlines()[PASSPHRASE_OUTPUT_LINE]
    assert result.exit_code == 0
    assert "_" in passphrase_output


def test_cli_prompting_number_of_words_if_not_provided():
    runner = CliRunner()
    result = runner.invoke(main, "--delimiter '_'", input="8\n")
    passphrase_output = result.output.splitlines()[PASSPHRASE_OUTPUT_LINE]
    passphrase_words = passphrase_output.split("_")
    assert result.exit_code == 0
    assert not result.exception
    assert len(passphrase_words) == 8


def test_cli_number_of_words():
    runner = CliRunner()
    result = runner.invoke(main, "--words 5 --delimiter '_'")
    passphrase_output = result.output.splitlines()[PASSPHRASE_OUTPUT_LINE]
    passphrase_words = passphrase_output.split("_")
    assert result.exit_code == 0
    assert len(passphrase_words) == 5


def test_cli_number_of_words_input_not_in_range():
    runner = CliRunner()
    result = runner.invoke(main, "--words 0")
    assert result.exit_code == 2  # usage error


def test_cli_number_of_words_input_not_a_number():
    runner = CliRunner()
    result = runner.invoke(main, "--words 'this is not a number!'")
    assert result.exit_code == 2  # usage error


def test_cli_capitalisation():
    runner = CliRunner()
    result = runner.invoke(main, "--words 5 --delimiter '_' --caps")
    passphrase_output = result.output.splitlines()[PASSPHRASE_OUTPUT_LINE]
    passphrase_words = passphrase_output.split("_")
    assert result.exit_code == 0
    for word in passphrase_words:
        if word[0].isalpha():
            assert word[0].isupper()


def test_cli_no_capitalisation():
    runner = CliRunner()
    result = runner.invoke(main, "--words 5 --delimiter '_' --no-caps")
    passphrase_output = result.output.splitlines()[PASSPHRASE_OUTPUT_LINE]
    passphrase_words = passphrase_output.split("_")
    assert result.exit_code == 0
    for word in passphrase_words:
        if word[0].isalpha():
            assert word[0].islower()


def test_cli_no_delimiter():
    runner = CliRunner()
    result = runner.invoke(main, "--words 5 --delimiter '' --caps")
    passphrase_output = result.output.splitlines()[PASSPHRASE_OUTPUT_LINE]
    assert result.exit_code == 0
    assert len(passphrase_output.split()) == 1
