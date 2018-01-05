# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.
'''
#alternate solution
def greatest(list_of_numbers):
    if list_of_numbers == []:
        return 0
    return max(list_of_numbers)
    '''
def greatest(list_of_numbers):
    big = 0
    for i in list_of_numbers:
        if i > big:
            big = i
    return big




print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0
