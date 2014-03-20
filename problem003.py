#!/usr/bin/python
'''
Created on Mar 18, 2014

@author: Daniel Corroto

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

from numberUtil import isPrime

def nextPrime(i):
    i += 2
    while not isPrime(i):
        i+= 2
    return i

def removeFactor(last,x,i):
    while x % i == 0:
        x /= i
        last = i
    return last, x

def getLargestPrimeFactor(x):
    last = 1
    last, x = removeFactor(last, x, 2)

    i = 3
    while x > 1:
        last, x = removeFactor(last, x, i)
        i = nextPrime(i)

    return last

print getLargestPrimeFactor(600851475143L)
