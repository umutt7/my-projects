from plates import is_valid

def test_length():
    assert is_valid("A") == False
    assert is_valid("AAAAAA2") == False
    assert is_valid("CS50") == True


def test_first_char_number():
    assert is_valid("0CS50") == False
    assert is_valid("00000") == False
    assert is_valid("CSP50") == True


def test_first_number_zero():
    assert is_valid("CS05") == False


def test_middle_number():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False


def test_symbols():
    assert is_valid("A CS") == False
    assert is_valid("HELLO!") == False


def test_begin_alpha():
    assert is_valid("CSCS12") == True
    assert is_valid("50") == False