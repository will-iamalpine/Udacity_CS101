# Double Gold Star

# Khayyam Triangle

# The French mathematician, Blaise Pascal, who built a mechanical computer in
# the 17th century, studied a pattern of numbers now commonly known in parts of
# the world as Pascal's Triangle (it was also previously studied by many Indian,
# Chinese, and Persian mathematicians, and is known by different names in other
# parts of the world).

# The pattern is shown below:
#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                   ...

# Each number is the sum of the number above it to the left and the number above
# it to the right (any missing numbers are counted as 0).

# Define a procedure, triangle(n), that takes a number n as its input, and
# returns a list of the first n rows in the triangle. Each element of the
# returned list should be a list of the numbers at the corresponding row in the
# triangle.

#my solution
def triangle(n):
    seed = [1,[1,1]]
    if n == 0:
        return []
    if n == 1:
        return([1])
    if n == 2:
        return seed
    if n > 2:
        #adding i rows to triangle
        for i in range(n-2):
            count = 0
            newlist = [1]
            #print 'repeat this operation',i+1,'times'
            for count in range(i+1):
                #print count,'count'
                #pulls value from the two upper legs of triangle
                value = seed[-1][count]+seed[-1][count+1]
                newlist.append(value)
                count +=1
                #print 'newcount',count
            newlist.append(1)
            #print newlist,'newlist'
            seed.append(newlist)
    return seed

#udacity solution
def make_next_row(row):
    result = []
    prev = 0
    for e in row:
        result.append(e+prev)
        prev = e
    result.append(prev)
    return result

def triangleUdacity(n):
    result = []
    current = [1]
    for unused in range(0,n):
        result.append(current)
        current = make_next_row(current)

    return result

#For example:

#print triangle(0)
#>>> []

#print triangle(1)
#>>> [[1]]

#print triangle(2)
#>> [[1], [1, 1]]

#print triangle(3)
#>>> [[1], [1, 1], [1, 2, 1]]

#print triangle(4)
#>>>[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

#print triangle(5)
#>>>[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]


#print triangle(6)
#>>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
