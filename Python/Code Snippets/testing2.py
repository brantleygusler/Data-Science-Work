"""
A test script to test the module funcs.py

Author: Brantley G. Gusler
Date: 1/1/2022
"""
import introcs      # For assert_equals and assert_true
import funcs        # This is what we are testing

def test_has_a_vowel():
    """
    Test procedure for has_a_vowel
    """
    print('Testing has_a_vowel')

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
    result = funcs.has_a_vowel('uuuu')
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

def test_has_y_vowel():
    """
    Test procedure for has_y_vowel
    """
    print('Testing has_y_vowel')

    #Test Case 1
    result = funcs.has_y_vowel('ydx')
    introcs.assert_equals(False,result)

    #Test Case 2
    result = funcs.has_y_vowel('eyae')
    introcs.assert_equals(True,result)

    #Test Case 3
    result = funcs.has_y_vowel('bald')
    introcs.assert_equals(False,result)

    #Test Case 4
    result = funcs.has_y_vowel('you')
    introcs.assert_equals(False,result)

    #Test Case 5
    result = funcs.has_y_vowel('yyayy')
    introcs.assert_equals(True,result)

# Script Code
test_has_a_vowel()
test_has_y_vowel()
print('Module funcs is working correctly')
