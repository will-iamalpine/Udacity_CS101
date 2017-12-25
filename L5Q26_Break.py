countdown = 10

'''while countdown >= 0:
    print countdown
    countdown = countdown - 1'''
    
#equivalent statement tests
'''while countdown >= 0:
    if False:
        break
    print countdown
    countdown = countdown - 1'''

#more tests
while countdown >= 0:
    print countdown
    countdown = countdown - 1
    if countdown >=0:
        print countdown
        countdown = countdown - 1
    else:
        break
