from .plates import is_valid

def test_plate_length():
    assert is_valid("AA") == True
    assert is_valid("A2") == False  # Too short
    assert is_valid("2A") == False  # Too short
    assert is_valid("22") == False  # Too short
    assert is_valid(" 2") == False  # Invalid character
    assert is_valid("ABC1234") == False  # Too long
    assert is_valid("ABC123") == True  # Valid length

def test_no_special_char():
    assert is_valid("$$") == False  # Special characters
    assert is_valid("DEF456") == True  # Valid alphanumerics
    assert is_valid("+ABCDE") == False  # Special character
    assert is_valid("ABC1 3") == False  # Space is a special character

def test_first_two_char_are_letters():
    assert is_valid("12ABCD") == False  # First two characters are digits
    assert is_valid("1ABCDE") == False  # First character is digit
    assert is_valid("ABCDE1") == True  # First two characters are letters

def test_first_number_not_zero():
    assert is_valid("ABC012") == False  # Leading zero
    assert is_valid("DEF123") == True  # Numbers at the end
    assert is_valid("AB1C") == False  # Numbers not at the end
    assert is_valid("ABCD12") == True  # Numbers at the end
