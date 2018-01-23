# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.

import re
# print re.split("[.+!]", "this.is+a!string")
#>>> 'this', 'is', 'a', 'string']

#my initial solution
def split_string(source,splitlist):
    #format for re.split by adding brackets around string
    split_list = '['+ splitlist + ']'
    #perform re.split procedure
    new_split = re.split(split_list, source)
    #filter empty values from list
    new_split = filter(None, new_split) # fastest
    return new_split

#Udacity solution
def split_string_udacity(source,splitlist):
        output = []
        atsplit = True
        for char in source:
            if char in splitlist:
                atsplit = True
            else:
                if atsplit:
                    output.append(char)
                    atsplit = False
                else:
                    output[-1] += char
        return output



out = split_string("This is a test-of the,string separation-code!"," ,!-")

print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']
