# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.


def print_numbers1(a):
    i = 1
    while i != a:
        print i
        i = i + 1
    return i

def print_numbers2(a):
    i = 1
    while i <= a:
        print i
        i = i + 1

#just experimenting
print(print_numbers1(3))
print_numbers1(3)

print_numbers2(3)
#>>> 1
#>>> 2
#>>> 3
