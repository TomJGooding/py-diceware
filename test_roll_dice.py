from roll_dice import Die


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
