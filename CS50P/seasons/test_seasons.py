from seasons import ask

def test_valid_dates():
    assert ask("1999-01-01") == "Five hundred twenty-five thousand, six hundred minutes"
    assert ask("2001-01-01") == "One million, fifty-one thousand, two hundred minutes"

