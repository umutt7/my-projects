from numb3rs import validate


def test_minus():
    assert validate("-1.1.1.1") == False
    assert validate("1.-1.1.1") == False
    assert validate("1.1.-1.1") == False
    assert validate("1.1.1.-1") == False


def test_aboves():
    assert validate("256.1.1.1") == False
    assert validate("1.256.1.1") == False
    assert validate("1.1.256.1") == False
    assert validate("1.1.1.256") == False


def test_texts():
    assert validate("cat") == False
    assert validate("cat.cat") == False
    assert validate("cat.cat.cat") == False
    assert validate("cat.cat.cat.cat") == False


def test_corrects():
    assert validate("23.120.255.1") == True
    assert validate("0.0.0.0") == True
    assert validate("63.118.242.8") == True


def test_wrongbytes():
    assert validate("1") == False
    assert validate("1.1.1.1.1") == False
