'''
Created on Mar 19, 2014

@author: Daniel Corroto

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

from numberUtil import primeGenerator

def getNthPrime(x):
    res = 0
    for i in primeGenerator(10001):
        res = i
    return res

print getNthPrime(10001)