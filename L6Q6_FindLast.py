# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.
'''
#a good solution from another student
def find_last(text, target):
    pos = -1
    while True:
		pos = text.find(target, pos + 1)
		if text.find(target, pos + 1) == -1:
			return pos
			break
'''
#Flipping the strings and starting the search that way. Woo!
def find_last(a,b):
    #flip both strings
    a_inv = a[::-1]
    b_inv = b[::-1]
    #the position starting from the end of the string counting backwards
    inv_pos = (a_inv.find(b_inv))
    #convert to counting frontwards by subtracting the length of string b
    #and the inv_pos counter from string a lengt
    position = (len(a)-inv_pos-len(b))
    if inv_pos == -1:
        return -1
    return (position)

    #print (a_inv)
    #print(len(a_inv))

print find_last('12345','321')
#>>> -1

print find_last("De l'audace, encore de l'audace, toujours de l'audace", 'audace')
#>>> 47

print find_last('aaaa', 'a')
#>>> 3

print find_last('aaaaa', 'aa')
#>>> 3

print find_last('aaaa', 'b')
#>>> -1

print find_last("111111111", "1")
#>>> 8

print find_last("222222222", "")
#>>> 9

print find_last("", "3")
#>>> -1

print find_last("", "")
#>>> 0
