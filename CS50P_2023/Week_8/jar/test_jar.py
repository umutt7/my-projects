from jar import Jar
import pytest

def test_init():
    jar = Jar()


def test_str():
    jar = Jar()
    assert str(jar) == ""
    assert jar.size == 0
    jar.deposit(1)
    assert str(jar) == "🍪"


def test_capacity():
    jar = Jar()
    assert jar.capacity == 12
    jar_high = Jar(13)
    assert jar_high.capacity == 13


def test_size():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.withdraw(2)
    assert jar.size == 3


def test_deposit():
    jar = Jar(5)
    with pytest.raises(ValueError):
        jar.deposit(7)


def test_withdraw():
    jar = Jar()
    jar.size = 6
    jar.withdraw(4)
    assert jar.size == 2