"""
The test script for the course project.

Author: Brantley G. Gusler
Date: 1/6/2022
"""
import introcs
import funcs

def test_matching_parens():
    """
    Test procedure for matching_parens
    """
    print('Testing matching_parens')

    #Test Case 1
    result = funcs.matching_parens('P (M) R')
    introcs.assert_equals(True,result)

    #Test Case 2
    result = funcs.matching_parens('() ( (')
    introcs.assert_equals(True,result)

    #Test Case 3
    result = funcs.matching_parens('T L M')
    introcs.assert_equals(False,result)

    #Test Case 4
    result = funcs.matching_parens('U Q )')
    introcs.assert_equals(False,result)

    #Test Case 5
    result = funcs.matching_parens('K ((O) (T))')
    introcs.assert_equals(True,result)

    #Test Case 6
    result = funcs.matching_parens('T (D P')
    introcs.assert_equals(False,result)

    #Test Case 7
    result = funcs.matching_parens('')
    introcs.assert_equals(False,result)

def test_first_in_parens():
    """
    Test procedure for first_in_parens
    """
    print('Testing first_in_parens')

    #Test Case 1
    result = funcs.first_in_parens('P (M) R')
    introcs.assert_equals('M',result)

    #Test Case 2
    result = funcs.first_in_parens('(J) I (X)')
    introcs.assert_equals('J',result)

    #Test Case 3
    result = funcs.first_in_parens('(T L M)')
    introcs.assert_equals('T L M',result)

    #Test Case 4
    result = funcs.first_in_parens('U Q ()')
    introcs.assert_equals('',result)

    #Test Case 5
    result = funcs.first_in_parens('K ((O) (T))')
    introcs.assert_equals('(O',result)



# Script Code
test_matching_parens()
test_first_in_parens()
print('Module funcs is working correctly')
