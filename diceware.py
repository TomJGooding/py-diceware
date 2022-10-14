class Passphrase:
    def __init__(self, number_of_words: int) -> None:
        self.number_of_words: int = number_of_words


def read_int(prompt: str, min_value: int = 1) -> int:
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            if value < min_value:
                print(f"The minimum passphrase length is {min_value}.")
            else:
                return value
        except ValueError:
            print("Please enter a number.")


def main() -> None:
    number_of_words = read_int("Number of words: ", min_value=1)
    passphrase = Passphrase(number_of_words)


if __name__ == "__main__":
    main()
