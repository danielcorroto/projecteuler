'''
Created on Mar 19, 2014

@author: Daniel Corroto


Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
'''
from numberUtil import getDivisors

def d(n):
    res = reduce(lambda x, y: x + y, getDivisors(n))
    return res - n

count = 0
for i in range(2,10000):
    a = d(i)
    if (a > i):
        b = d(a)
        if (b == i and b < 10000):
            count += a+b

print count