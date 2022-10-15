PASSPHRASE_DEFAULTS: dict = {
    "number_of_words": 6,
    "min_words": 1,
    "delimiter": "",
}


class Passphrase:
    def __init__(self, number_of_words: int, delimiter: str) -> None:
        self.number_of_words: int = number_of_words
        self.delimiter: str = delimiter


def is_valid_int(user_input: str, min_value) -> bool:
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


def read_number_of_words(prompt: str):
    while True:
        user_input = input(prompt)
        if user_input == "":
            return PASSPHRASE_DEFAULTS["number_of_words"]
        if is_valid_int(
            user_input,
            min_value=PASSPHRASE_DEFAULTS["min_words"],
        ):
            return int(user_input)


def read_delimiter(prompt: str) -> str:
    delimiter: str = input(prompt)
    return delimiter


def main() -> None:
    number_of_words = read_number_of_words(
        f"Number of words (default={PASSPHRASE_DEFAULTS['number_of_words']}): "
    )
    delimiter = read_delimiter(
        f"Delimiter (default=\"{PASSPHRASE_DEFAULTS['delimiter']}\"): "
    )
    passphrase = Passphrase(number_of_words, delimiter)


if __name__ == "__main__":
    main()
