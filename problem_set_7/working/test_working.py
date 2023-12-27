from working import convert

def test_12_to_24():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_12_to_24_short():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_forget_to():
    try:
        convert("9 AM - 5 PM")
        raise Exception("Did not raise ValueError")
    except ValueError:
        pass

def test_invalid_time():
    try:
        convert("9:00 AM to 25:00 PM")
        raise Exception("Did not raise ValueError")
    except ValueError:
        pass

def test_invalid_format():
    try:
        convert("9:00xm to 5:00 pm")
        raise Exception("Did not raise ValueError")
    except ValueError:
        pass
