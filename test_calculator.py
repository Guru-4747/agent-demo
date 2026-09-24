from calculator import average


def test_positive_numbers():
    assert average([2, 4, 6]) == 4


def test_single_number():
    assert average([5]) == 5


def test_negative_numbers():
    assert average([-2, -4, -6]) == -4


def test_decimal_numbers():
    assert average([1.5, 2.5]) == 2
