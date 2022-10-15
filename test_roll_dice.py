from roll_dice import Dice, Die


def test_die_with_set_face():
    die = Die(face=1)
    assert die.face == 1


def test_die_roll_always_valid_face():
    die = Die(sides=1)
    for _ in range(100):
        assert die.roll() == 1


def test_die_to_string(capfd):
    die = Die(face=3)
    print(die)
    out, _ = capfd.readouterr()
    assert out == "3\n"


def test_dice():
    dice = Dice(num_dice=5, sides=1)
    for die in dice.dice:
        assert die.face == 1


def test_dice_to_string(capfd):
    dice = Dice(num_dice=5, sides=1)
    print(dice)
    out, _ = capfd.readouterr()
    assert out == "11111\n"
