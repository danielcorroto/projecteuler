'''
Created on Mar 27, 2014

@author: Daniel Corroto

The first two consecutive numbers to have two distinct prime factors are:
14 = 2 * 7
15 = 3 * 5
The first three consecutive numbers to have three distinct prime factors are:
644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.
Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
'''
from numberUtil import getProperDivisors, isPrime

i = 1
count = 0
while True:
    divisors = sum([1 for j in getProperDivisors(i) if isPrime(j)])
    count += 1 if divisors == 4 else -count
    if count == 4:
        print i - 3
        break
    i += 1
