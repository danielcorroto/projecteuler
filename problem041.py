'''
Created on Mar 23, 2014

@author: Daniel Corroto

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?
'''
from numberUtil import isPrime

def getPandigital(x, maxi):
    found = -1
    s = str(x)
    if len(s) == maxi and isPrime(x):
        return x
    for i in range(maxi, 0, -1):
        if found == -1 and s.find(str(i)) == -1:
            temp = x
            x = x * 10 + i
            found = getPandigital(x, maxi)
            x = temp
    return found

found = -1
i = 9
while found == -1 and i > 0:
    found = getPandigital(0, i)
    i -= 1

print found
