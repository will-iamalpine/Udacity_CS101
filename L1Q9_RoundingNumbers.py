# Given a variable, x, that stores the
# value of any decimal number, write Python
# code that prints out the nearest whole
# number to x.
# If x is exactly half way between two
# whole numbers, round up, so
# 3.5 rounds to 4 and 2.5 rounds to 3.
# You may assume x is not negative.

# Hint: The str function can convert any number into a string.
# eg str(89) converts the number 89 to the string '89'

# Along with the str function, this problem can be solved
# using just the information introduced in unit 1.

# x = 3.14159
# >>> 3 (not 3.0)
# x = 27.63
# >>> 28 (not 28.0)
# x = 3.5
# >>> 4 (not 4.0)

x = 3.4

print int(x+0.5)

#floor solution of 0.5 found here: https://stackoverflow.com/questions/31818050/python-2-7-round-number-to-nearest-integer
#turns out it was also in the solutions as well
