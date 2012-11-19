"""
Implement an algorithm to verify the correctness of a Sudoku puzzle solution

sudoku solution in 9 x 9 array

- check rows
- check columns
- check 3x3
- sum all elements

Assumption - user knows how to play sudoku - input 1-9
"""


def check_rows(sudoku):
    for i in sudoku:
        if len(set(i)) < 9:
            return False
    return True
        

def check_columns(sudoku):
    for i in xrange(0,9):
        columns = [sudoku[j][i] for j in xrange(0,9)]
        if len(set(columns)) < 9:
            return False
    return True 


# 3 x 3 grid
def check_mini(sudoku):
    for i in xrange(0, 3):
        nums = []
        for x in xrange(i*3, i*3 + 3):
            for y in xrange(i*3, i*3 + 3):
                n = sudoku[x][y]
                if n in nums:
                    return False
                else:
                    nums.append(n)
        if len(nums) != 9:
            return False
    return True

def is_solved(sudoku):
    print check_mini(sudoku)
    return check_rows(sudoku) and check_columns(sudoku) and check_mini(sudoku) 
    
correct_solution = [[9, 6, 3, 1, 7, 4, 2, 5, 8], 
                    [1, 7, 8, 3, 2, 5, 6, 4, 9], 
                    [2, 5, 4, 6, 8, 9, 7, 3, 1], 
                    [8, 2, 1, 4, 3, 7, 5, 9, 6], 
                    [4, 9, 6, 8, 5, 2, 3, 1, 7], 
                    [7, 3, 5, 9, 6, 1, 8, 2, 4], 
                    [5, 8, 9, 7, 1, 3, 4, 6, 2], 
                    [3, 1, 7, 2, 4, 6, 9, 8, 5], 
                    [6, 4, 2, 5, 9, 8, 1, 7, 3]]
wrong_solution =   [[9, 6, 3, 1, 7, 4, 2, 5, 8], 
                    [1, 7, 8, 3, 2, 5, 6, 4, 9], 
                    [2, 5, 4, 6, 8, 9, 7, 3, 1], 
                    [8, 2, 1, 4, 3, 7, 5, 9, 6], 
                    [4, 9, 6, 5, 5, 2, 3, 1, 7], 
                    [7, 3, 5, 9, 6, 1, 8, 2, 4], 
                    [5, 8, 9, 7, 1, 3, 4, 6, 2], 
                    [3, 1, 7, 2, 4, 6, 9, 8, 5], 
                    [6, 4, 2, 5, 9, 8, 1, 7, 3]]

print is_solved(correct_solution)
print is_solved(wrong_solution)
