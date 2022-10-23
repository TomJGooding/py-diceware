import click

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


@click.command()
@click.option(
    "-w",
    "--words",
    type=click.IntRange(min=1),
    default=PASSPHRASE_DEFAULTS.number_of_words,
    prompt="Number of words",
    help="Number of words for passphrase.",
    show_default=True,
)
@click.option(
    "-d",
    "--delimiter",
    default=PASSPHRASE_DEFAULTS.delimiter,
    prompt=True,
    prompt_required=False,
    help="Delimiter to separate words in passphrase.",
    show_default=True,
)
@click.option(
    "--caps/--no-caps",
    default=PASSPHRASE_DEFAULTS.capitalisation,
    help="Capitalise words in passphrase.",
    show_default=True,
)
def main(words, delimiter, caps):
    """Diceware passphrase generator."""
    click.echo(TITLE_BANNER)

    click.echo(f"Rolling dice {words} times...")
    dice_rolls: list[Dice] = roll_dice(words)
    for dice in dice_rolls:
        click.echo(dice)

    click.echo("\nLooking up words...")
    wordlist = PASSPHRASE_DEFAULTS.wordlist
    passphrase = Passphrase(
        words,
        delimiter,
        caps,
        dice_rolls,
        wordlist,
    )
    for idx, word in enumerate(passphrase.words):
        click.echo(f"{dice_rolls[idx]}  {word}")

    click.echo("\nYour passphrase is:")
    click.echo(passphrase)
