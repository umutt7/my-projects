from working import convert
import pytest


def test_no_minutes():
    assert convert("9 AM to 10 AM") == "09:00 to 10:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_with_minutes():
    assert convert("9:30 AM to 10:30 AM") == "09:30 to 10:30"
    assert convert("12:30 AM to 12:30 PM") == "00:30 to 12:30"


def test_valueerror():
    with pytest.raises(ValueError):
        convert("9AM to 10AM")
    with pytest.raises(ValueError):
        convert("25:30 AM to 10:30 AM")
    with pytest.raises(ValueError):
        convert("13 am to 53 pm")
    with pytest.raises(ValueError):
        convert("9:70 am to 5:00 pm")


def test_omit():
    with pytest.raises(ValueError):
        convert("9 am to 10")
    with pytest.raises(ValueError):
        convert("9 am 4 pm")
