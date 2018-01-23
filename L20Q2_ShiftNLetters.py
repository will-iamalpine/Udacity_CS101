# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    letter = ord(letter)
    total = letter + n
    if total > 122:
        total = 96 + (total - 122)
    if total < 97:
        total = 122-(96-total)
    return chr(total)

'''
print shift_n_letters('s', 13)
#>>> f
print shift_n_letters('a', -2)
#>>> y
print shift_n_letters('a', -1)
#>>> z
print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i
'''
