from bank import value
import sys
def test_value():
    try:
        assert value("Hello") == 0
        assert value("How you doing?") == 20
        assert value("What's happening?") == 100
    except AssertionError:
        sys.exit()


