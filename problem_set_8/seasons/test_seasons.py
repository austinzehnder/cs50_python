from datetime import date
from seasons import get_age_in_minutes, format_age

def test_get_age_in_minutes():
    birthdate = date(2022, 1, 2)
    actual = get_age_in_minutes(birthdate)
    expected = 1052640
    assert actual == expected

def test_format_age():
    minutes = 52526400
    actual = format_age(minutes)
    expected = "Fifty-two million, five hundred twenty-six thousand, four hundred"
    assert actual == expected

