"""
A function to check the validity of a numerical string

Author: Brantley G. Gusler
Date: 2/11/2012
"""
import introcs


def valid_format(s):
    """
    Returns True if s is a valid numerical string; it returns False otherwise.

    A valid numerical string is one with only digits and commas, and commas only
    appear at every three digits.  In addition, a valid string only starts with
    a 0 if it has exactly one character.

    Pay close attention to the precondition, as it will help you (e.g. only numbers
    < 1,000,000 are possible with that string length).

    Examples:
        valid_format('12') returns True
        valid_format('apple') returns False
        valid_format('1,000') returns True
        valid_format('1000') returns False
        valid_format('10,00') returns False
        valid_format('0') returns True
        valid_format('012') returns False

    Parameter s: the string to check
    Precondition: s is nonempty string with no more than 7 characters
    """

    if s[0] == '0':
        return s == '0'

    if len(s) <= 3:
        result = introcs.isdigit(s)

    elif s[-4] != ',':
        result = False

    else:
        result = introcs.isdigit(s[:-4]) and introcs.isdigit(s[-3:])

    return result
