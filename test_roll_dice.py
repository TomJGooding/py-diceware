from roll_dice import Dice, Die, roll_dice


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
    for die in dice.faces:
        assert die.face == 1


def test_dice_to_string(capfd):
    dice = Dice(num_dice=5, sides=1)
    print(dice)
    out, _ = capfd.readouterr()
    assert out == "11111\n"


def test_roll_dice_6_rolls_5_dice():
    num_rolls = 6
    num_dice = 5
    faces = 1

    dice_rolls = roll_dice(num_rolls, num_dice, faces)
    assert len(dice_rolls) == 6
    for dice in dice_rolls:
        for die in dice.faces:
            assert die.face == 1


def test_roll_dice_100_rolls_100_dice():
    num_rolls = 100
    num_dice = 100
    faces = 1

    dice_rolls = roll_dice(num_rolls, num_dice, faces)
    assert len(dice_rolls) == 100
    for dice in dice_rolls:
        for die in dice.faces:
            assert die.face == 1
