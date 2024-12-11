from square import get_square

# the function should also start with test_***()
def test_sq2():
    x=2
    res = get_square(x)
    assert res == 4 # testing part
    assert get_square(9) == 81

def test_sq():
    x=5
    res = get_square(x)
    assert res == 25 # testing part
    assert get_square(3) == 9

