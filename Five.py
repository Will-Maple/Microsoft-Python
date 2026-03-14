import pytest

def contains_five(numbers):
    if 5 in numbers:
        return True
    else:
        return False

def test_contains_five():
    my_list = [1, 3, 5, 7, 9]
    assert contains_five(my_list) is True