# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?

def is_palindrome(s):
    #if len(s) >=2:
    #    print s, 'len',len(s),'string',s[0], 'vs', s[-1]
    if len(s) == 0 or len(s) == 1:
        return True
    if len(s) == 2:
        if s[0] != s[-1]:
            return False
        return True
    return is_palindrome(s[1:-1])


print is_palindrome('')
#>>> True
print is_palindrome('andrea')
#>>> False
print is_palindrome('a')
#>>> True
print is_palindrome('abab')
#>>> False
print is_palindrome('abba')
#>>> True
print is_palindrome('12321')
#>>True
print is_palindrome('123321')
#>>> True
