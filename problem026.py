'''
Created on Mar 19, 2014

@author: Daniel Corroto

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
    1/2    =     0.5
    1/3    =     0.(3)
    1/4    =     0.25
    1/5    =     0.2
    1/6    =     0.1(6)
    1/7    =     0.(142857)
    1/8    =     0.125
    1/9    =     0.(1)
    1/10    =     0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''
from numberUtil import primeGenerator

def getCicleLength(x):
    found = [-1 for _ in range(x)]
    rem = 1 % x
    count = 0
    while rem > 0 and found[rem] == -1:
        found[rem] = count
        rem = rem * 10 % x
        count += 1
    return count - found[rem] if rem > 0 else 0

num, length = (0, 0)
for i in xrange(3, 1001, 2):
    l = getCicleLength(i)
    if (l > length):
        num, length = (i, l)
    if (i > 1000):
        break

print num, length
