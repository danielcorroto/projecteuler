'''
Created on Mar 27, 2014

@author: Daniel Corroto

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
What 12-digit number do you form by concatenating the three terms in this sequence?
'''
from numberUtil import primeGenerator, isPrime

def xrangeExclude(mini, maxi, *excl):
    count = mini
    while count < maxi:
        if not count in excl:
            yield count
        count += 1

def getPermutations(x):
    res = []
    a = (x / 1000, x / 100 % 10, x / 10 % 10, x % 10)

    for i in xrangeExclude(0, 4):
        for j in xrangeExclude(0, 4, i):
            for k in xrangeExclude(0, 4, i, j):
                for l in xrangeExclude(0, 4, i, j, k):
                    if not l in (i, j, k):
                        y = a[i] * 1000 + a[j] * 100 + a[k] * 10 + a[l]
                        if y > 1000 and isPrime(y) and not y in res:
                            res.append(y)

    return res

for i in primeGenerator(10000):
    if i > 1000:
        l = getPermutations(i)
        for j in l:
            if j > i:
                diff = j - i
                if j + diff > j and j + diff in l:
                    print i, j, j + diff
