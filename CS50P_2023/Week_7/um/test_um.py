from um import count
import pytest


def test_count():
    assert count("um") == 1
    assert count("um um") == 2
    assert count("um um um") == 3
    assert count("um um um um") == 4


def test_um_in_words():
    assert count("gum") == 0
    assert count("bum") == 0
    assert count("bumblebee") == 0


def test_um_followed_by_punctuation():
    assert count("um.") == 1
    assert count("um, um!") == 2


def test_um_case_insensitive():
    assert count("UM") == 1
    assert count("Um") == 1
    assert count("uM") == 1
    assert count("Um uM") == 2
