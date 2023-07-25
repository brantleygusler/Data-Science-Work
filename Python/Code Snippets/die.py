"""
A simple die roller

Author: Brantley Gusler
Date: 12/17/2021
"""
x = input('Type the first number: ')
first = int(x)
y = input('Type the last number: ')
last = int(y)
import random
roll = random.randint(first,last)
print ('Choosing a number between '+str(first)+' and '+str(last) +'.')
print ('The number is'+' '+str(roll)+'.')
