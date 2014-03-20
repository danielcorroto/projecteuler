'''
Created on Mar 18, 2014

@author: Daniel Corroto
'''

import math


if __name__ == '__main__':
    pass

def isPrime(x):
    if (x < 2):
        return False
    elif (x == 2):
        return True
    elif (x % 2 == 0):
        return False

    maxi = math.sqrt(x)
    i = 3
    while i <= maxi:
        if (x % i == 0):
            return False
        i += 2

    return True

def primeGenerator(maxi=-1):
    yield 2
    count = 1
    i = 3
    while (maxi < 0 or count < maxi):
        if isPrime(i):
            yield i
            count += 1
        i += 2


def isPalindrome(x):
    xx = x
    y = 0
    while xx > 0:
        y = y * 10 + xx % 10
        xx /= 10

    return x == y

def getDivisors(x):
    result = []
    for i in range(1, int(math.sqrt(x) + .5) + 1):
        if (x % i == 0):
            result.append(i)
            if (i * i != x):
                result.append(x / i);
    return result;

def getProperDivisors(x):
    result = []
    for i in range(1, int(math.sqrt(x) + .5) + 1):
        if (x % i == 0):
            result.append(i)
            if (i * i != x and i != 1):
                result.append(x / i);
    return result;
