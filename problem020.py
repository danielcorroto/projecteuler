'''
Created on Mar 19, 2014

@author: Daniel Corroto

n! means n * (n - 1) * ... * 3 * 2 * 1
For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!
'''

from math import factorial

def sumDigits(x):
    count = 0
    while (x > 0):
        count += x % 10
        x /= 10
    return count

print sumDigits(factorial(100))