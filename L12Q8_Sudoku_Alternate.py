# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

#My personal approach to the sudoku problem, outputs the row or column of failure

#checks for repeated numbers in a list
#does not output True
def check_range(listinput):
    for x in range(1,len(listinput)+1):
        if listinput.count(x) != 1:
            #print listinput.count(x)
            return False
        else:
            continue

#checks all lists within matrix for check_range
def check_horizontal(matrix):
    for i in matrix:
        if check_range(i) is False:
            print False, ', failed in row', matrix.index(i)+1
            return False
        else:
            continue

def check_vertical(matrix):
    if check_horizontal(matrix) != False:
        newlist = []
        y = 0
        while y < len(matrix):
            for i in matrix:
                newlist.append(i[y])
                if len(newlist) == len(matrix):
                    if check_range(newlist) != False:
                        #print newlist
                        newlist = []
                        y += 1
                    else:
                        print False,', failed column', y+1
                        return False
    else:
        return False


def check_sudoku(matrix):
    if check_vertical(matrix) != False:
        print 'Passed!'


correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect1 = [[1,2,1,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

#fail on row 2
incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]



check_sudoku(correct)
#>>> True

check_sudoku(incorrect)
#>>> False

check_sudoku(incorrect1)
#>>> False

check_sudoku(incorrect2)
# False for 3rd column

check_sudoku(incorrect2)
#>>> False

check_sudoku(incorrect3)
#>>> False

check_sudoku(incorrect4)
#>>> False

check_sudoku(incorrect5)
#>>> False
