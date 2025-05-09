from twttr import shorten

def test_letters():
    assert shorten("Hello") == "Hll"
    assert shorten("HI") == "H"
    assert shorten("aeiou") == ""


def test_numbers():
    assert shorten("123") == "123"


def test_punctuation():
    assert shorten("Hello! How are you?") == "Hll! Hw r y?"