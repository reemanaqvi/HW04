#!/usr/bin/env python
# HW04_ex08_11

# The following functions are all intended to check whether a string contains 
# any lowercase letters, but at least some of them are wrong. For each function, 
# describe what the function actually does (assuming that the parameter is a
# string).

# Do not merely paste the output as a counterexample into the documentation 
# string, explain what is wrong.

################################################################################
# Body

def any_lowercase1(s):
    """This will only run once to check the first letter of the string is lowercase because 'return' will exit out of the for loop after one run. So, 'House' would return false because it won't check 'ouse'
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    """This creats a new string'c' and only checks if it is lowercase. The answer will always be True no matter what s is.  
    """
    for c in s:
        if 'c'.islower():
            return 'True'   
        else:
            return 'False'

def any_lowercase3(s):
    """This one goes letter by letter and returns the case for the last letter only. So for 'girL', it would return False
    """
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    """This should work. flag is set False but in the for statement, if c.islower() becomes True even once, flag cannot be reassigned False after that
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    """This checks the whole word and if any letter is uppercase, returns False
    """
    for c in s:
        if not c.islower():
            return False
    return True

################################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong, 
    # call that function with a string for which the function returns
    # incorrectly. ex.: any_lowercase_("thisstringmessesupthefunction")
    any_lowercase1("checK")
    any_lowercase2("CAT")
    any_lowercase3("gitS")
    any_lowercase4("worKsFine")
    any_lowercase5("faILs")
    

if __name__ == '__main__':
    main()