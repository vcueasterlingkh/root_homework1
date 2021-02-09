"""Test cases are important."""


from homework1 import hw1



def test_return_number_3():
    assert hw1.return_number_3() == 3

def test_return_string_vcu():
    assert hw1.return_string_vcu() == "vcu"

def test_return_lowercased_string():
    assert hw1.return_lowercased_string("HI THERE MOM") == "hi there mom"


def test_return_without_starting_ending_whitespace(input_string):
    assert hw1.return_without_starting_ending_whitespace("   asdfasdf    ") == "asdfasdf"

def test_return_addition():
    assert hw1.return_addition(1, 2) == 3


