'''
Created on Mar 20, 2014

@author: Daniel Corroto

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

'''
top left
    (i * 2 - 1) * (i * 2 - 1) - 2 * (i - 1)
top right
    (i * 2 - 1) * (i * 2 - 1)
bottom left
    (i * 2 - 1) * (i * 2 - 1) - 4 * (i - 1)
bottom right
    (i * 2 - 1) * (i * 2 - 1) - 6 * (i - 1)
'''

print sum(4 * (i * 2 - 1) * (i * 2 - 1) - 12 * (i - 1) for i in xrange(2, 1001 // 2 + 2)) + 1
