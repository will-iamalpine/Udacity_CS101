###############################################
#       Exercise by Websten from forums       #
###############################################
# A palindrome is a word or a phrase that reads
# the same backwards as forwards. Make a program
# that checks if a word is a palindrome.
# If the word is a palindrome, print 0 to the terminal,
# -1 otherwise.
# The word contains lowercase letters a-z and
# will be at least one character long.
#
### HINT! ###
# You can read a string backwards with the following syntax:
# string[::-1] - where the "-1" means one step back.
# This exercise can be solved with only unit 1 knowledge
# (no loops or conditions)

word = "madam"
# test case 2
# word = "madman" # uncomment this to test
inverse_word = word[::-1]
###
# YOUR CODE HERE. DO NOT DELETE THIS LINE OR ADD A word DEFINITION BELOW IT.
###

is_palindrome = inverse_word.find(word)

# TESTING
print is_palindrome
# >>> 0  # outcome if word == "madam"
# >>> -1 # outcome if word == "madman"


#function version for fun...
def fun_is_palindrome(word):
    if word == inverse_word :
        return True
    return False

print (fun_is_palindrome(word))
