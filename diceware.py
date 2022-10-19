import cli
from config import PASSPHRASE_DEFAULTS
from passphrase import Passphrase
from roll_dice import Dice, roll_dice


def main() -> None:
    print(cli.TITLE_BANNER)

    # Read passphrase options from the user
    number_of_words: int = cli.read_number_of_words(
        f"Number of words (default={PASSPHRASE_DEFAULTS.number_of_words}): "
    )
    delimiter: str = cli.read_delimiter(
        f'Delimiter (default="{PASSPHRASE_DEFAULTS.delimiter}"): '
    )
    capitalisation: bool = cli.read_capitalisation("Capitalise words? [Y/n] ")
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


if __name__ == "__main__":
    main()
