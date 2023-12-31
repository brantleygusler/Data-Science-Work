"""
A function with several helpers.

The primary function in this module is str_to_seconds.  The functions get_hours,
get_minutes, and get_seconds are all helper functions that are used to implement
this function.  They should implemented in the order listed.

Author: Brantley G. Gusler
Date: 1/6/2022
"""
import introcs


def iso_8601(s):
    """
    Returns True if s is a string in ISO 8601 format, False otherwise

    Parameter time: The string to check
    Precondition: s is a string of length 8
    """
    assert type(s) == str, repr(s)+' is not a string.'
    assert len(s) == 8, repr(s)+' The string has the wrong amount of characters.'

    check1 = introcs.isdigit(s[:2])
    check2 = s[2] == ':'
    check3 = introcs.isdigit(s[3:4])
    check4 = s[5] == ':'
    check5 = introcs.isdigit(s[6:7])
    return check1 and check2 and check3 and check4 and check5


def get_seconds(time):
    """
    Returns the number of seconds in the string time (as an int).

    The value time is a string in extended ISO 8601 format.  That is, it has the form
    'hh:mm:ss' where h, m, and s are digits.  There must be exactly two digits each for
    hours, minutes, and seconds, so they are padded with 0s when necessary.
    leading 0s if they are only one digit, but there may be only one hour digit. For
    more information, see

        https://en.wikipedia.org/wiki/ISO_8601#Times

    This function does not support time zones, abbreviated formats, or decimals

    Example: get_seconds('12:35:15') returns 15
    Example: get_seconds('03:02:05') returns 5
    Example: get_seconds('00:00:00') returns 0

    Parameter time: The string representation of the time
    Precondition: time is a string in extended ISO 8601 format 'hh:mm:ss'
    """
    assert type(time) == str, repr(time)+' is not a string.'
    assert len(time) == 8, repr(time)+' The string has the wrong amount of characters.'
    assert iso_8601(time), repr(time)+' has the wrong format'

    result = int(time[6:])
    return result


def get_minutes(time):
    """
    Returns the number of minutes in the string time (as an int).

    The value time is a string in extended ISO 8601 format.  That is, it has the form
    'hh:mm:ss' where h, m, and s are digits.  There must be exactly two digits each for
    hours, minutes, and seconds, so they are padded with 0s when necessary.
    leading 0s if they are only one digit, but there may be only one hour digit. For
    more information, see

        https://en.wikipedia.org/wiki/ISO_8601#Times

    This function does not support time zones, abbreviated formats, or decimals

    Example: get_minutes('12:35:15') returns 35
    Example: get_minutes('03:02:05') returns 2
    Example: get_minutes('00:00:00') returns 0

    Parameter time: The string representation of the time
    Precondition: time is a string in extended ISO 8601 format 'hh:mm:ss'
    """
    assert type(time) == str, repr(time)+' is not a string.'
    assert len(time) == 8, repr(time)+' The string has the wrong amount of characters.'
    assert iso_8601(time), repr(time)+' has the wrong format'

    result = int(time[3:5])
    return result

def get_hours(time):
    """
    Returns the number of hours in the string time (as an int).

    The value time is a string in extended ISO 8601 format.  That is, it has the form
    'hh:mm:ss' where h, m, and s are digits.  There must be exactly two digits each for
    hours, minutes, and seconds, so they are padded with 0s when necessary.
    leading 0s if they are only one digit, but there may be only one hour digit. For
    more information, see

        https://en.wikipedia.org/wiki/ISO_8601#Times

    This function does not support time zones, abbreviated formats, or decimals

    Example: get_hours('12:35:15') returns 12
    Example: get_hours('03:02:05') returns 3
    Example: get_hours('00:00:00') returns 0

    Parameter time: The string representation of the time
    Precondition: time is a string in extended ISO 8601 format 'hh:mm:ss'
    """
    assert type(time) == str, repr(time)+' is not a string.'
    assert len(time) == 8, repr(time)+' The string has the wrong amount of characters.'
    assert iso_8601(time), repr(time)+' has the wrong format'

    result = int(time[:2])
    return result


def str_to_seconds(time):
    """
    Returns the number of seconds since midnight in the string time (as an int).

    The value time is a string in extended ISO 8601 format.  That is, it has the form
    'hh:mm:ss' where h, m, and s are digits.  There must be exactly two digits each for
    hours, minutes, and seconds, so they are padded with 0s when necessary.  So
    seconds, minutes, and hours may have leading 0s if they are only one digit. For
    more information, see

        https://en.wikipedia.org/wiki/ISO_8601#Times

    This function does not support time zones, abbreviated formats, or decimals
    """

    Example: str_to_seconds('12:35:15') returns 45315
    Example: str_to_seconds('03:02:05') returns 10925
    Example: str_to_seconds('00:00:00') returns 0

    Parameter time: The string representation of the time
    Precondition: time is a string in extended ISO 8601 format 'hh:mm:ss'
    """
    assert type(time) == str, repr(time)+' is not a string.'
    assert len(time) == 8, repr(time)+' The string has the wrong amount of characters.'
    assert iso_8601(time), repr(time)+' has the wrong format'

    a = get_seconds(time)
    b = get_minutes(time)*60
    c = (get_hours(time)*60)*60
    result = a + b + c
    return int(result)
