"""
see if given maze is solvable

input: maze NxN
output: True if maze is solvable
        False if not

other things to think about - should we make some restrictions
to size of a maze - it could take too long to see if it is solvable?
"""


def is_maze_solvable(maze):
    # check input maze
    if maze is None or len(maze) < 1 or len(maze[0]) < 1:
        return False

    # find starting point 'S'
    start_x = -1
    start_y = -1

    for i in xrange(len(maze)):
        for j in xrange(len(maze[0])):
            if maze[i][j] == 'S':
                start_x = i
                start_y = j

    if start_x == -1:
        return False

    return explore_maze(maze, start_x, start_y)

def explore_maze(maze, x, y):
    #print maze, x, y
    # cannot explore beyond maze boundaries
    if x < 0 or x > len(maze) - 1 or y < 0 or y > len(maze) - 1:
        return False

    # cannot explore in direction with * 
    if maze[x][y] == '*':
        return False

    if maze[x][y] == 'E':
        return True

    # put current element in maze as * to prevent cycles
    maze[x][y] = '*'

    if explore_maze(maze, x, y+1): return True
    if explore_maze(maze, x, y-1): return True
    if explore_maze(maze, x+1, y): return True
    if explore_maze(maze, x-1, y): return True

    return False


# test maze - solvable
maze1 = [['*', '*', '*', '*', '*', '', '', ''],
         ['*', '', '', '', '*', '', '', ''],
         ['*', 'S', '*', '*', '*', '', '', ''],
         ['*', '', '', '', '*', '*', '*', '*'],
         ['*', '', '*', '', '', '', '', '*'],
         ['*', '', '', '', '*', '', '', '*'],
         ['*', '*', '*', '*', '*', '', 'E','*'],
         ['', '', '', '', '*', '*', '*', '*']
        ]

print is_maze_solvable(maze1)

# test maze - unsolvable
maze2 = [['*', '*', '*', '*', '*', '', '', ''],
         ['*', '', '', '', '*', '', '', ''],
         ['*', 'S', '*', '*', '*', '', '', ''],
         ['*', '', '', '', '*', '*', '*', '*'],
         ['*', '', '*', '', '', '', '', '*'],
         ['*', '*', '*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '', 'E','*'],
         ['', '', '', '', '*', '*', '*', '*']
        ]
print is_maze_solvable(maze2)
 
