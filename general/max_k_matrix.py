"""
How can you efficiently determine the k-th maximum element in a MxN sorted matrix?
1  2   6 10
3  4   7 13
5  9  11 14
8 12  15  16
"""
from heapq import heappush
from heapq import heappop

def max_k(matrix, k):
    # checking
    if matrix is None or len(matrix) < 1 or len(matrix[0]) < 1:
        return False
    if k is None or k < 1:
        return False

    m = len(matrix)
    n = len(matrix[0])
    if k > m * n :
        return False
    
    visited = [(matrix[m-1][n-1], m-1, n-1)]
    children = []

    # we are sure it will end eventually because it's checked earlier
    while len(visited) < k:
        # take the last element that is visited
        element, i, j = visited[-1]
        if i - 1 >= 0 and (-1 * matrix[i-1][j], i-1, j) not in children:
            heappush(children, (-1 * matrix[i-1][j], i-1, j))
        if j - 1 >= 0 and (-1 * matrix[i][j-1], i, j-1) not in children:
            heappush(children, (-1 * matrix[i][j-1], i, j-1))
        max_child, i, j = heappop(children)
        visited.append((-1 * max_child, i, j))
        
            
    return visited[-1][0]



matrix = [[1, 2, 6, 10],
          [3, 4, 7, 13],
          [5, 9, 11, 14],
          [8, 12, 15, 16]]

k = 5

print max_k(matrix, k)
