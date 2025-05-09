from bank import value

def test_hello():
    assert value("HELLO") == 0
    assert value("hello") == 0


def test_h():
    assert value("hi") == 20
    assert value("H") == 20


def test_nonh():
    assert value("good morning") == 100
    assert value("ciao") == 100