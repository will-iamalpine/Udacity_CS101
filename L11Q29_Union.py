# Define a procedure, union,
# that takes as inputs two lists.
# This is a modification from the original exercise that
#does not modify the original list



def union(a,b):
    i = 0
    union = list(a)
    for find in b:
        if find not in a:
            union.append(b[i])
        i += 1
    return union

a = [1,2,3]
b = [2,4,6]

print union(a,b)
#>>> [1,2,3,4,6]

print a
#>>> [1,2,3]
print b
#>>> [2,4,6]
