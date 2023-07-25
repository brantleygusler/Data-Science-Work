"""
The functions for the course project.

Author: Brantley G. Gusler
Date: 1/7/2022
"""
import introcs

def matching_parens(n):
    """
    Returns True if the string s has a matching pair of parentheses.

    A matching pair pair of parentheses is an open parens '(' followed by a closing
    parens ')'.  Any thing can be between the two pair (including other parens).

    Example: matching_parens('A (B) C') returns True
    Example: matching_parens('A )B( C') returns False

    Parameter s: The string to check
    Precondition: s is a string (possibly empty)
    """
    assert type(n) == str, repr(n)+' is not a string.'

    # Search for the first open parens '('
    a = introcs.find_str(n,'(')
    # Search for the first close parens ')' AFTER the open parens
    b = introcs.find_str(n,')',a)
    # Compare both searches to -1 and return True if BOTH are not -1
    result = a != -1 and b !=-1
    return result



def first_in_parens(s):
    """
    Returns: The substring of s that is inside the first pair of parentheses.

    The first pair of parenthesis consist of the first instance of character
    '(' and the first instance of ')' that follows it.

    Example: first_in_parens('A (B) C') returns 'B'
    Example: first_in_parens('A (B) (C)') returns 'B'
    Example: first_in_parens('A ((B) (C))') returns '(B'

    Parameter s: a string to check
    Precondition: s is a string with a matching pair of parens '()'.
    """
    assert type(s) == str, repr(s)+' is not a string.'
    assert introcs.count_str(s,'(') >= 1, 'The string '+repr(s)+' does not have an opening paren.'
    d = introcs.find_str(s,'(') + 1
    assert introcs.count_str(s,')',d) >= 1, 'The string '+repr(s)+' does not have a closing paren.'

    a = introcs.find_str(s,'(') + 1
    b = introcs.find_str(s,')',a)
    slice = s[a:b]
    return slice
