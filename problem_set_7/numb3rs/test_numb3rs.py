from numb3rs import validate

def test_validate_digits():
    assert validate("0.0.0.0") == True
    assert validate("127.0.0.1") == True
    assert validate("125.0.0.266") == False
    assert validate("256.0.0.0") == False
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False

def test_validate_letters():
    assert validate("a.0.0.0") == False
    assert validate("0.a.0.0") == False
    assert validate("0.0.a.0") == False
    assert validate("0.0.0.a") == False
    assert validate("cat") == False
