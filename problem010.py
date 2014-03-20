'''
Created on Mar 19, 2014

@author: Daniel Corroto

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

from numberUtil import primeGenerator

def sumPrimeUnder(x):
    res = 0
    for i in primeGenerator():
        if (i < x):
            res += i
        else:
            return res

print sumPrimeUnder(2000000)
