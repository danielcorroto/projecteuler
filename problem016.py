'''
Created on Mar 19, 2014

@author: Daniel Corroto

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
'''

def sumBiPower(x):
    y = 2 ** x
    temp = 0
    while y > 0:
        temp += y % 10
        y /= 10
    return temp

print sumBiPower(1000)