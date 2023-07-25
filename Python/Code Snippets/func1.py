"""
Author: Brantley Gusler
Date: 12/29/2021

"""
import random

def rollem(first,last):
    """
    Generates two random numbers, adds them, and displays the result.

    The numbers generated are between first and last (inclusive).

    Example: For the call rollem(1,6), the displayed output may be

    Choosing two numbers between 1 and 6.
    The sum is 11.

    Parameter first: The lowest possible number
    Precondition: first is an integer

    Parameter last: The greatest possible number
    Precondition: last is an integer, last >= first
    """
    num1 = random.randint(first,last)
    num2 = random.randint(first,last)
    thesum = num1+num2
    print('Choosing two numbers between '+str(first)+' and '+str(last)+'.')
    print('The sum is '+str(thesum)+'.')
