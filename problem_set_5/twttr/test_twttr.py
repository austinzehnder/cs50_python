from twttr import shorten


def test_no_vowels():
    assert shorten("twttr") == "twttr"

def test_numbers():
    assert shorten("123") == "123"

def test_punctuation():
    assert shorten("Hi!") == "H!"

def test_mixed():
    assert shorten("Hi there? 456") == "H thr? 456"

def test_capitalized_vowels():
  assert shorten("HAllO") == "Hll"
