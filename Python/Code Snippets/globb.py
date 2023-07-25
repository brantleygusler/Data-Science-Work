"""
A module to demonstrate global variables.

Author: Brantley Gusler
Date: 12/31/2021
"""

# The global variable
VAR = 1

def next():
    """
    Returns and increments the value of VAR.
    """
    global VAR
    result = VAR
    VAR = VAR+1
    return result
