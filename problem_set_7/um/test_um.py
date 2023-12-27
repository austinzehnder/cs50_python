from um import count

def test_um():
    assert count("um") == 1

def test_um_and_char():
    assert count("um?") == 1

def test_um_with_spaces():
    assert count(" um ") == 1

def test_um_case():
    assert count("UM") == 1

def test_um_in_word():
    assert count("um crumb") == 1
