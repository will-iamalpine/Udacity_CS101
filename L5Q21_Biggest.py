# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest(a,b,c):
    if a >= b:
        if a >= c:
            return a
        elif a < c:
            return c
    else:
        if b <= c:
            return c
        elif b > c:
            return b

print biggest(3, 6, 9)

#better solution:
print max(3, 6, 9)
#>>> 9

#print biggest(6, 9, 3)
#>>> 9

#print biggest(9, 3, 6)
#>>> 9

#print biggest(3, 3, 9)
#>>> 9

#print biggest(9, 3, 9)
#>>> 9
