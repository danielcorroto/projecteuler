'''
Created on Mar 19, 2014

@author: Daniel Corroto


A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def pythagoreanTriplet(x):
    for c in range(x + 1):
        for b in range(x + 1 - c):
            a = x - c - b
            if (c * c == b * b + a * a):
                return a * b * c

print pythagoreanTriplet(1000)
