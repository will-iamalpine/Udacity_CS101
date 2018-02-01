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

#my bloated solution in progress...need to revisit and use recursion
def deep_reverse(input_list):
    '''
    newlist = []
    print 'input_list:',input_list, 'length:',len(input_list)
    if input_list == [] : #stopping case
        return newlist

    if is_list(input_list[-1]) == False: #integer at end, append
        print input_list[-1],'adding to newlist'
        newlist.append(input_list[-1])
        return newlist + deep_reverse(input_list[:-1])

    if is_list(input_list[-1]) == True and is_list(input_list[-1][-1]) == False: #no more nested lists
        print 'end of list:',input_list[-1]
        toadd = input_list[-1][::-1]
        print toadd, 'toadd', type(toadd)
        newlist.append(toadd)
        return newlist + deep_reverse(input_list[:-1])

    if is_list(input_list[-1][-1]) == True: #if nested list
        print 'else case'
        return newlist + deep_reverse(input_list[-1]) #return next level down

    #now need to work on crawling back up recursively
    #return deep_reverse(input_list)

#this alternate solution is incorrect, since it modifies the original list in-place using reverse()
def deep_reverse(input_list):
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
    return a'''

#Udacity solution
def deep_reverseUdacity(input_list):
    if is_list(input_list):
        result = []
        for i in range(len(input_list)-1, -1, -1): #for loop in reverse order
            print i,'i'
            result.append(deep_reverse(input_list[i]))
            print result
    else:
        return input_list

#For example,
#p = [1, [2, 3, [4, [5, 6]]]]
#print deep_reverseUdacity(p)
#>>> [[[[6, 5], 4], 3, 2], 1]
#print p,'p'
#>>> [1, [2, 3, [4, [5, 6]]]]

#q =  [1, [2,3], 4, [5,6]]
#print deep_reverseUdacity(q)
#>>> [ [6,5], 4, [3, 2], 1]
#print q,'q'
#>>> [1, [2,3], 4, [5,6]]
