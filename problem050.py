'''
Created on Mar 27, 2014

@author: Daniel Corroto

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.
The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''
from numberUtil import primeGenerator, isPrime

primesum = []
count = 0
for i in primeGenerator(1000000):
    count += i
    primesum.append(count)

number = 0
maxi = 0
for i in xrange(len(primesum)):
    for j in xrange(i, len(primesum)):
        if primesum[j] - primesum[i] > 1000000:
            break
        if j - i > maxi and isPrime(primesum[j] - primesum[i]):
            maxi = j - 1
            number = primesum[j] - primesum[i]

print maxi, number
