class Passphrase:
    def __init__(self, number_of_words: int) -> None:
        self.number_of_words: int = number_of_words


def is_valid_int(user_input: str, min_value: int = 1) -> bool:
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


def read_int(prompt: str) -> int:
    while True:
        user_input = input(prompt)
        if is_valid_int(user_input, min_value=1):
            return int(user_input)


def main() -> None:
    number_of_words = read_int("Number of words: ")
    passphrase = Passphrase(number_of_words)


if __name__ == "__main__":
    main()
