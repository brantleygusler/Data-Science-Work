"""
A function to search for the first vowel position

Author2/11/2022
"""
import introcs


def first_vowel(s):
    """
    Returns the position of the first vowel in s; it returns -1 if there are no vowels.

    We define the vowels to be the letters 'a','e','i','o', and 'u'.  The letter
    'y' counts as a vowel only if it is not the first letter in the string.

    Examples:
        first_vowel('hat') returns 1
        first_vowel('grrm') returns -1
        first_vowel('sky') returns 2
        first_vowel('year') returns 1

    Parameter s: the string to search
    Precondition: s is a nonempty string with only lowercase letters
    """

    result = len(s) #in case there is no 'a'

    if 'a' in s:
        result = introcs.find_str(s,'a')

    if 'e' in s[:result]:
        result = introcs.find_str(s,'e'[:result])

    if 'i' in s[:result]:
        result = introcs.find_str(s,'i'[:result])

    if 'o' in s[:result]:
        result = introcs.find_str(s,'o'[:result])

    if 'u' in s[:result]:
        result = introcs.find_str(s,'u'[:result])

    if 'y' in s[1:result]:
        result = introcs.find_str(s,'y',1)

    return result if 'a' in s or 'e' in s or 'i' in s or 'o' in s or 'u' in s or 'y' in s[1:] else -1
