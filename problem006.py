#!/usr/bin/python
'''
Created on Mar 18, 2014

@author: Daniel Corroto

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def sumOfSquare(x):
    temp = 0
    for i in range(1, x + 1):
        temp += i * i
    return temp

def squareOfSum(x):
    return ((x * x + x) / 2) ** 2

print squareOfSum(100) - sumOfSquare(100)
