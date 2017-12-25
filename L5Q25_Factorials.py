# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

print factorial(4)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
#>>> 720
