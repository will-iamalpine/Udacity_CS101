# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(input,key):
    i = 0
    for e in input:
        if e == key:
            return i
        i += 1
    return -1
#my solution
    '''count = 0
    for P in input:
        if input[count] == key:
            return count
        else:
            count += 1
    return -1'''


print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta', 'epsilon' ,'gamma'],'gamma')
#>>> -3

print find_element(['alpha','beta', 'epsilon'],'gamma')
#>>> -1
