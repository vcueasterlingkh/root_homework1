""" This set of functions should return the appropriate data type"""


def return_number_3():
    """ This function should return an integer with the value of 3"""

    return_value = 3
    return return_value


def return_string_vcu():
    """ This function should return a string with the lowercase value of vcu"""

    return_value = "vcu"
    return return_value


def return_lowercased_string(input_string):
    """You have a variable called input_string that is of type string.
    Return it but the lowercase version of it."""
    str = "HI THERE MOM"
    return_value = (str.lower())
    return return_value


def return_without_starting_ending_whitespace(input_string): 
    """You have a variable called input_string that is of type string.
    Return it but with the surrounding (left and right) whitespace stripped."""
    str = "   asdfasdf    "
    return_value = (str.strip())
    return return_value


def return_addition(x,y):
    """ Return the two numbers added together. """
    total = x + y
    return_value = total
    return return_value
