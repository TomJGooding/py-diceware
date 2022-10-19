from config import PASSPHRASE_DEFAULTS

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
