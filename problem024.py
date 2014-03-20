'''
Created on Mar 19, 2014

@author: Daniel Corroto

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

count = 0

def findLexicographic(l, level, count, x):
    if level == 10:
        count += 1
        if count == 1000000:
            print x
            return count, x

    found = 0
    for i in range(10):
        if not l[i] and found == 0:
            l[i] = True
            temp = x
            x = x * 10 + i
            count, found = findLexicographic(l, level + 1, count, x)
            x = temp
            l[i] = False

    return count, found

findLexicographic([False for i in xrange(10)], 0, 0, 0)
