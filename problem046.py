'''
Created on Mar 26, 2014

@author: Daniel Corroto

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
9 = 7 + 2*1^2
15 = 7 + 2*2^2
21 = 3 + 2*3^2
25 = 7 + 2*3^2
27 = 19 + 2*2^2
33 = 31 + 2*1^2
It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''
from numberUtil import isPrime, primeGenerator
from math import sqrt

def compositeGenerator(maxi=-1):
    i = 9
    while (maxi < 0 or i < maxi):
        if not isPrime(i):
            yield i
        i += 2

def checkGoldbach(x):
    for i in primeGenerator(x):
        y = sqrt((x - i) / 2.0)
        if int(y) == y:
            return True
    return False

for i in compositeGenerator():
    if not checkGoldbach(i):
        print i
        break
