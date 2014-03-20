#!/usr/bin/python
'''
Created on Mar 18, 2014

@author: Daniel Corroto

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

def sumDivisible(x):
    maxi = 999 // x
    return x * ((maxi*maxi+maxi) // 2)

x = sumDivisible(3) + sumDivisible(5) - sumDivisible(15)
print x
