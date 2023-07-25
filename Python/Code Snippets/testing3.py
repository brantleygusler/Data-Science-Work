"""
A test script to test the module func.py

Author: Brantley G. Gusler
Date: 1/1/2022
"""
import introcs      # For assert_equals and assert_true
import funcs        # Testing funcs


def test_replace_first():
    """
    Test procedure for replace_first
    """
    print('Testing replace_first')

    # Test Case 1
    result = funcs.replace_first('crane','a','o')
    introcs.assert_equals('crone',result)

    # Test Case 2
    result = funcs.replace_first('poll','l','o')
    introcs.assert_equals('pool',result)

    # Test Case 3
    result = funcs.replace_first('crane','cr','b')
    introcs.assert_equals('bane',result)

    # Test Case 4
    result = funcs.replace_first('hat','h','f')
    introcs.assert_equals('fat',result)

    # Test Case 5
    result = funcs.replace_first('fars','far','bat')
    introcs.assert_equals('bats',result)

    # Test Case 6
    result = funcs.replace_first('goo','o','l')
    introcs.assert_equals('glo',result)

    # Test Case 7
    result = funcs.replace_first('axxxa','axxx','b')
    introcs.assert_equals('ba',result)

    # Test Case 8
    result = funcs.replace_first('twenty','y','y two')
    introcs.assert_equals('twenty two',result)

# Script Code
# Calling module tests
test_replace_first()
print('Module funcs is working correctly')
