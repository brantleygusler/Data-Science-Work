"""
An empty module to illustrate function stubs.

This module will contain function stubs, which are callable but do not do anything.

Name: Brantley G. Gusler
Date: 1/3/2022
"""
import introcs

def initials(n):
    """
    Returns: The initials <first>. <last>. of the given name.

    We assume that n is just two names (first and last). Middle names are
    not supported.

    Example: initials('John Smith') returns 'J. S.'
    Example: initials('Walker White') returns 'W. W.'

    Parameter n: the person's name
    Precondition: n is in the form 'first-name last-name' with one space
    between names. There are no spaces in either <first-name> or <last-name>
    """
    # Find the first initial (and assign it to 'first')
    first = n[0]
    # Find the position of the last name (and assign it to 'pos')
    pos = introcs.rfind_str(n,' ')+1
    # Find the last initial (and assign it to 'last')
    last = n[pos]
    # Compute the final answer (and assign it to 'result')
    result = first + '. ' + last + '.'
    # Return the answer
    return result
