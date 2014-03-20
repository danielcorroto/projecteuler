#!/usr/bin/python
'''
Created on Mar 18, 2014

@author: Daniel Corroto

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
def getFactorsGenerator(x):
    yield 1
    while (x > 1 and x % 2 == 0):
        yield 2
        x /= 2;

    i = 3;
    while x > 1:
        if (x % i == 0):
            yield i
            x /= i;
        else:
            i += 2;

def mcm(x, y):
    a, b = (x, y) if x < y else (y, x)

    res = b;
    for l in getFactorsGenerator(a):
        if b % l == 0:
            b /= l;
        else:
            res *= l;

    return res;

def smallestEvenlyDivisible(x):
    res = 1
    for i in range(1, x + 1):
        res = mcm(res, i)
    return res

print smallestEvenlyDivisible(20)
