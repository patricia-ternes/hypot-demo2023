
# test addition
def test_addition_int():
    assert addition(4,7) == 4

def test_addition_float():
    assert addition(2.3, 7.92) == 10.22

def test_addition_str():
    assert addition("a", "b") == "Please just use integer or float"

# test squared
def test_squared_odd():
    assert squared(3) == 9

def test_squared_even():
    assert squared(4) == 16

def test_squared_negative():
    assert squared(-2) == 4

# test squared root
def test_sqroot():
    assert sqroot(9) == 3 

# test hypot
def test_hypot():
    hypot(3,4) == 5