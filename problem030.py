'''
Created on Mar 20, 2014

@author: Daniel Corroto

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

def isFifthPower(x):
    temp = 0
    temp = x
    while x > 0:
        temp += (x % 10) ** 5
        x //= 10
    return temp == temp

print sum([i for i in xrange(10, 10 ** (5 + 1)) if isFifthPower(i)])
