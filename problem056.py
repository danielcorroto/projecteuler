'''
Created on Apr 24, 2014

@author: Daniel Corroto

A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

'''

def digitalSum(x):
    result = 0
    while x > 0:
        result += x % 10
        x /= 10
    return result

sums = [digitalSum(i ** j) for i in range(100) for j in range(100)]
print max(sums)
