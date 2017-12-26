# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# The Python code should be general enough
# to pass every possible case where 'zip'
# can occur in a string

# Here are two example test cases:
#text = 'all zip files are zipped'
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

str1 = "all zip files are compressed"
str2 = "zip";

first_str = str1.find('zip')
print str1.find(str2,first_str+1)
#print str1.find(str2)
#print str1.find(str2, 10)
#print str1.find(str2, 40)


'''
here are some learning attempts for posterity

offset=5
cut=text[offset:]
searchy = cut.find('zip')+offset

print(searchy)

if cut.find('zip') == True:
    print(searchy)
else:
    print('fail')


# IMPORTANT BEFORE SUBMITTING:
# You should only have one print command in your function'''
