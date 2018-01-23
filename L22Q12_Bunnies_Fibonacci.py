# Define a procedure, fibonacci, that takes a natural number as its input, and
# returns the value of that fibonacci number.

# Two Base Cases:
#    fibonacci(0) => 0
#    fibonacci(1) => 1

# Recursive Case:
#    n > 1 : fibonacci(n) => fibonacci(n-1) + fibonacci(n-2)

#my initial solution without using recursion
def fibonacci(n):
    counter=[0,1]
    for i in range(n-1):
        counter.append(counter[-1]+counter[-2])
    return counter#[n]

#udacity recursive solution
def fibonacci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

#udacity solution
def fibonacciUdacity(n):
    current = 0
    after = 1
    for i in range(n):
        current, after = after, after + current
    return current




#quiz: how many times is fibonacci(30) counted recursively in evaluating fibonacci_recursive(36)?
#print fibonacci(36-30+1) #working backwards on counter list starting from counter[1]
#>>> 13

#print fibonacci(0)
#>>> 0
#print fibonacci(1)
#>>> 1
#print fibonacci(2)
#>>> 1
#print fibonacci_recursive(3)
#>>> 2
#print fibonacci_recursive(4)
#>>> 3
#print fibonacci_recursive(5)
#>>> 5
#print fibonacci_recursive(6)
#>>> 8
#print fibonacci(7)
#>>> 13
#print fibonacci_recursive(7)
#>>> 13
#print fibonacciUdacity(7)
#>>> 13
#print fibonacci(15)
#>>> 610
#print fibonacci_recursive(15)
#>>> 610
#print fibonacciUdacity(15)
#>>> 610
#print fibonacci_recursive(36)
