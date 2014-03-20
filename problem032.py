'''
Created on Mar 20, 2014

@author: Daniel Corroto

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

def isPandigital(x, y, z):
    return "".join(sorted(str(x) + str(y) + str(z))) == "123456789"

temp = 0
for i in xrange(1234, 9877):
    for j in xrange(1, 99):
        if i % j == 0 and isPandigital(i, j, i // j):
            temp += i
            break

print temp
