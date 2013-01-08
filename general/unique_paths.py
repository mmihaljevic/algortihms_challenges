"""
Imagine a robot sitting on the upper left hand corner of an NxN grid. The robot can
only move in two directions: right and down. How many possible paths are there for
the robot?

Idea:
for each path that is done - add one 
if path cannot be completed - add 0

"""

def unique_robot_paths(grid):
    if grid is None or len(grid) < 1 or len(grid[0]) < 1:
        return False
    
    if len(grid) != len(grid[0]):
        return False

    return explore_grid(grid, 0, 0)

def explore_grid(grid, x, y):
    if x > len(grid) - 1 or y > len(grid) - 1:
        return 0

    if x == len(grid) - 1 and y == len(grid) - 1:
        return 1

    return explore_grid(grid, x, y+1) + explore_grid(grid, x+1, y)


# grid with only one element - one path
grid = [[0]]

print unique_robot_paths(grid)

# grid with N = g
grid = [[0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0]]

print unique_robot_paths(grid)

