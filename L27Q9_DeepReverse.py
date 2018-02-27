# Question 9: Deep Reverse
# Define a procedure, deep_reverse, that takes as input a list,
# and returns a new list that is the deep reverse of the input list.
# This means it reverses all the elements in the list, and if any
# of those elements are lists themselves, reverses all the elements
# in the inner list, all the way down.

# Note: The procedure must not change the input list.

# The procedure is_list below is from Homework 6. It returns True if
# p is a list and False if it is not.

def is_list(p):
    return isinstance(p, list)

def deep_reverse(input_list):
    copy,reverse = [],[]
    if is_list(input_list):
        for i in input_list:
            copy.append(i)
        while copy != []:
            reverse.append(deep_reverse(copy.pop()))
    else:
        reverse = input_list
    return reverse

#this alternate solution is incorrect, as it modifies the original list in-place
def deep_reverseAlternate(input_list):
    a = input_list
    a.reverse()
    print a,'a'
    for i in a:
        if is_list(i):
            print i,'i'
            deep_reverse(i)
            print a
        else:
            print a
    return a

#Udacity solution
def deep_reverseUdacity(input_list):
    if is_list(input_list):
        result = []
        for i in range(len(input_list)-1, -1, -1): #for loop in reverse order
            #print i,'i'
            result.append(deep_reverseUdacity(input_list[i]))
            #print result,'result'
        return result
    else:
        return input_list

#For example,
p = [1, [2, 3, [4, [5, 6]]]]
print deep_reverse(p)
#>>> [[[[6, 5], 4], 3, 2], 1]
#print p,'p'
#>>> [1, [2, 3, [4, [5, 6]]]]
#q =  [1, [2,3], 4, [5,6]]
#print deep_reverse(q)
#>>> [ [6,5], 4, [3, 2], 1]
#print q,'q'
#>>> [1, [2,3], 4, [5,6]]
