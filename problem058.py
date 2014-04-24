'''
Created on Apr 24, 2014

@author: Daniel Corroto


Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ~ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
'''
from numberUtil import isPrime

size = 1
sideprimes = 0

while sideprimes == 0 or sideprimes * 10 > 2 * size - 1:
    size += 2
    diagonales = [size * size - 3 * (size - 1), size * size - 3 * (size - 1) + size + size - 2, size * size - 3 * (size - 1) + size - 1]
    sideprimes += len([1 for d in diagonales if isPrime(d)])

print size, sideprimes
