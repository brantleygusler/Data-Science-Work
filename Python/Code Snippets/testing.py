"""
A test script to test the module funcs.py

Author: Brantley G Gusler
Date: 1/1/2022
"""
import introcs      # For assert_equals
import funcs        # This is what we are testing


# Put your code below this line
#Test Case 1
result = funcs.has_a_vowel('aeiou')
introcs.assert_equals(True,result)

#Test Case 2
result = funcs.has_a_vowel('toad')
introcs.assert_equals(True,result)

#Test Case 3
result = funcs.has_a_vowel('foot')
introcs.assert_equals(True,result)

#Test Case 4
result = funcs.has_a_vowel('gout')
introcs.assert_equals(True,result)

#Test Case 5
result = funcs.has_a_vowel('elephant')
introcs.assert_equals(True,result)

#Test Case 6
result = funcs.has_a_vowel('aaaa')
introcs.assert_equals(True,result)

#Test Case 7
result = funcs.has_a_vowel('qqyyii')
introcs.assert_equals(True,result)

#Test Case 8
result = funcs.has_a_vowel('aqueous')
introcs.assert_equals(True,result)

#Test Case 9
result = funcs.has_a_vowel('bcd')
introcs.assert_equals(False,result)

#Test Case 10
result = funcs.has_a_vowel('gym')
introcs.assert_equals(False,result)

result = funcs.has_a_vowel('aeiou')
introcs.assert_equals(True,result)

# Do not write below this line
print('Module funcs is working correctly')
