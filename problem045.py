'''
Created on Mar 23, 2014

@author: Daniel Corroto

Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
Triangle           T_n=n(n+1)/2          1, 3, 6, 10, 15, ...
Pentagonal         P_n=n(3n-1)/2         1, 5, 12, 22, 35, ...
Hexagonal          H_n=n(2n-1)           1, 6, 15, 28, 45, ...
It can be verified that T_285 = P_165 = H_143 = 40755.
Find the next triangle number that is also pentagonal and hexagonal.
'''
from math import sqrt

def getTriangular(x):
    return x * (x + 1) // 2

def isPentagonal(x):
    y = (sqrt(1 + 24 * x) + 1) / 6
    return int(y) * int(y) == y * y

def isHexagonal(x):
    y = (sqrt(1 + 8 * x) + 1) / 4
    return int(y) * int(y) == y * y

i = 285
while True:
    i += 1
    t = getTriangular(i)
    if isPentagonal(t) and isHexagonal(t):
        print t
        break
