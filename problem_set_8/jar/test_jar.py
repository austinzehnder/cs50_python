from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar._capacity == 12

    with pytest.raises(ValueError):
        Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.deposit(3)


def test_withdraw():
    jar = Jar(5)
    jar.deposit(3)
    jar.withdraw(1)
    assert jar.size == 2

    with pytest.raises(ValueError):
        jar.withdraw(3)

