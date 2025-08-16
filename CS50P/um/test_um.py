from um import count
def test_um():
    assert count("um") == 1
    assert count("um, um") == 2
    assert count("um, hello") == 1
    assert count("Um,hello, um, um?") == 3
    assert count("um.py") == 1
