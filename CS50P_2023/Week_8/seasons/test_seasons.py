from seasons import subtract_dates
import pytest


def test_valid_date():
    assert (
        subtract_dates("1998-06-22")
        == "Thirteen million, two hundred three thousand, three hundred sixty minutes"
    )
    assert (
        subtract_dates("2000-01-01")
        == "Twelve million, three hundred ninety-nine thousand, eight hundred forty minutes"
    )


def test_value_error():
    with pytest.raises(ValueError):
        subtract_dates("0000-00-00")
    with pytest.raises(ValueError):
        subtract_dates("1987-13-22")
    with pytest.raises(ValueError):
        subtract_dates("1987-12-32")
