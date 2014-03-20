'''
Created on Mar 20, 2014

@author: Daniel Corroto

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''
from numberUtil import isPrime, primeGenerator

def isTruncablePrime(x):
    y = x
    while x > 10:
        x = x / 10
        y = int(str(y)[1:])if y > 10 else 0
        if (not isPrime(x) or not isPrime(y)):
            return False
    return True

count = 0
temp = 0
for i in primeGenerator():
    if i > 10 and isTruncablePrime(i):
        temp += i
        count += 1
        if count == 11:
            break

print temp
