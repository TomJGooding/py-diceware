from py_diceware.config import PASSPHRASE_DEFAULTS
from py_diceware.passphrase import Passphrase
from py_diceware.roll_dice import Dice, roll_dice

TITLE_BANNER = r"""
    _______
  /\       \                            _ _
 /()\   ()  \     _ __  _   _        __| (_) ___ _____      ____ _ _ __ ___
/    \_______\   | '_ \| | | |_____ / _` | |/ __/ _ \ \ /\ / / _` | '__/ _ \
\    /()     /   | |_) | |_| |_____| (_| | | (_|  __/\ V  V / (_| | | |  __/
 \()/   ()  /    | .__/ \__, |      \__,_|_|\___\___| \_/\_/ \__,_|_|  \___|
  \/_____()/     |_|    |___/

"""


def is_valid_int(user_input: str, min_value: int) -> bool:
    result: bool = False
    try:
        value = int(user_input)
        if value < min_value:
            print(f"The minimum value is {min_value}.")
        else:
            result = True
    except ValueError:
        print("Please enter a number.")

    return result


def is_valid_y_or_n(user_input: str) -> bool:
    result: bool = False
    if user_input.lower() not in ("y", "n", "yes", "no"):
        print("Please answer yes or no.")
    else:
        result = True

    return result


def read_number_of_words(prompt: str) -> int:
    while True:
        user_input = input(prompt)
        if user_input == "":
            return PASSPHRASE_DEFAULTS.number_of_words
        if is_valid_int(
            user_input,
            min_value=PASSPHRASE_DEFAULTS.min_words,
        ):
            return int(user_input)


def read_delimiter(prompt: str) -> str:
    delimiter: str = input(prompt)
    return delimiter


def read_capitalisation(prompt: str) -> bool:
    while True:
        user_input = input(prompt)
        if user_input == "":
            return PASSPHRASE_DEFAULTS.capitalisation
        if is_valid_y_or_n(user_input):
            return True if user_input.lower() in ("y", "yes") else False


def main() -> None:
    print(TITLE_BANNER)

    # Read passphrase options from the user
    number_of_words: int = read_number_of_words(
        f"Number of words (default={PASSPHRASE_DEFAULTS.number_of_words}): "
    )
    delimiter: str = read_delimiter(
        f'Delimiter (default="{PASSPHRASE_DEFAULTS.delimiter}"): '
    )
    capitalisation: bool = read_capitalisation("Capitalise words? [Y/n] ")
    wordlist = PASSPHRASE_DEFAULTS.wordlist

    print("\nRolling dice...")
    dice_rolls: list[Dice] = roll_dice(number_of_words)

    print("\nLooking up words...")
    passphrase = Passphrase(
        number_of_words,
        delimiter,
        capitalisation,
        dice_rolls,
        wordlist,
    )

    print("\nYour passphrase is:")
    print(passphrase)