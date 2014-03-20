'''
Created on Mar 20, 2014

@author: Daniel Corroto

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
'''

from numberUtil import isPrime, primeGenerator

def isCircularPrime(x):
    orig = x
    length = len(str(x))
    power = 10 ** (length - 1)
    x = x // 10 + x % 10 * power
    while x != orig:
        if not isPrime(x):
            return False
        x = x // 10 + x % 10 * power
    return True

print sum([1 for i in primeGenerator(1000000) if isCircularPrime(i)])
