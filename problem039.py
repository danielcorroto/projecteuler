'''
Created on Mar 20, 2014

@author: Daniel Corroto

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p <= 1000, is the number of solutions maximised?
'''

from math import sqrt

count = [0 for i in xrange(1001)]

for c in xrange(1, 1001):
    for b in xrange(1, min(c, (1000 - c) / 2 + 1)):
        a = int(sqrt(c * c - b * b))
        if a + b + c <= 1000 and a * a + b * b == c * c:
            count[a + b + c] += 1
            break

maxi = 0
res = 0
for i in xrange(len(count)):
    if count[i] > maxi:
        maxi = count[i]
        res = i

print res
