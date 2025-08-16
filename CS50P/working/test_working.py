from working import convert
import pytest
def test_check():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("8 AM to 5 PM") == "08:00 to 17:00"
    assert convert("7 AM to 5 PM") == "07:00 to 17:00"
    assert convert("6 AM to 5 PM") == "06:00 to 17:00"
    assert convert("2 AM to 5 PM") == "02:00 to 17:00"
def test_convert_invalid_format():
    with pytest.raises(ValueError):
        convert("4AM to 5PM")
    with pytest.raises(ValueError):
        convert("4 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("0 AM to 8 PM")

