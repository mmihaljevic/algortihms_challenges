"""
1.7. 
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column is set to 0

Idea: 
a) Have an additional matrix and go trough all elements in MxN matrix and set zeroes 
b) For each element you go trough - check if it is on a 'zero line' (has zero on 
   it's column or row - do AND operator and if it is zero - put that element 
   zero)

"""

def matrix_zero(matrix):
    if matrix is None or len(matrix) < 1:
        return False

    m = len(matrix)
    n = len(matrix[0])
    init_zeros_x = []
    init_zeros_y = []

    for i in xrange(m):
        for j in xrange(n):
            # check if value is initially 0
            if matrix[i][j] == 0:
                if i not in init_zeros_x:
                    init_zeros_x.append(i)
                if j not in init_zeros_y:
                    init_zeros_y.append(j)
            elif i in init_zeros_x or j in init_zeros_y:
                matrix[i][j] = 0
            else:
                column = [matrix[x][j] for x in xrange(i,m) ]
                value_i = reduce(lambda x, y: x and y, column)
                value_j = reduce(lambda x, y: x and y, matrix[i][j:])
                value = value_i and value_j
                if value == 0:
                    matrix[i][j] = 0

    return matrix



matrix = [[1, 2, 1, 3, 2, 1, 1], 
          [3, 5, 0, 1, 5, 0, 1],
          [2, 1, 4, 6, 1, 1, 2],
          [5, 1, 1, 1, 0, 1, 1],
          [1, 2, 2, 0, 1, 1, 0]]

result = [[1, 2, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [2, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0]]

print "method result",  matrix_zero(matrix)
print "expected result", result
