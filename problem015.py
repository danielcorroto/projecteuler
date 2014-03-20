'''
Created on Mar 19, 2014

@author: Daniel Corroto

Starting in the top left corner of a 2*2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20*20 grid?
'''
def getRoutes(size):
    size += 1
    grid = [[0 for _ in xrange(size)] for _ in xrange(size)]
    grid[0][0] = 1

    for i in xrange(size):
        for j in xrange(size):
            if i > 0:
                grid[i][j] += grid[i - 1][j]
            if j > 0:
                grid[i][j] += grid[i][j - 1]


    return grid[size - 1][size - 1]

print getRoutes(20)
