from plates import is_valid

import sys
def test_plate():
        try:
                assert is_valid("CS50") == True
                assert is_valid("50FD") == False
                assert is_valid("PIE.14") == False
                assert is_valid("OUTATIME") == False
                assert is_valid("CS05") == False
                assert is_valid("F111") == False
                assert is_valid("001F") == False
                assert is_valid("CS50P") == False
        except AssertionError:
                sys.exit()
