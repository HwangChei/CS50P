from project import maximum

def test_maximum():
    assert maximum(1,2,3,4) == f'UTILITY HAS THE HIGHEST EXPENSES BEING 💲{4}'

def test_maximum2():
    assert maximum(4,3,2,1) == f'GROCERY HAS THE HIGHEST EXPENSES BEING 💲{4}'

def test_equal():
    assert maximum(1,1,1,1) == "EVERY EXPENSES ARE EQUAL"
