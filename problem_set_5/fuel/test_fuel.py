import pytest
from .fuel import convert, gauge


def test_convert_valid():
    assert convert("3/4") == 75
    assert convert("0/4") == 0
    assert convert("99/100") == 99

def test_convert_invalid():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("1/a")
    with pytest.raises(ValueError):
        convert("1/2.5")
    with pytest.raises(ValueError):
        convert("3/2")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
