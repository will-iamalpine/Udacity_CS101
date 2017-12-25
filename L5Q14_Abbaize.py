# Define a procedure, abbaize, that takes
# two strings as its inputs, and returns
# a string that is the first input,
# followed by two repetitions of the second input,
# followed by the first input.




def abbaize(a,b):
    #return str(a) + 2*str(b) + str(a)
    return str(a+2*b+a)

print abbaize('a','b')
#>>> 'abba'
print abbaize('dog','cat')
#>>> 'dogcatcatdog'
