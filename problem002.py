#!/usr/bin/python
'''
Created on Mar 18, 2014

@author: Daniel Corroto

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

def fibonacciGenerator(maxi):
    a=0
    b=1
    while (b <= maxi):
        c = a+b
        if c % 2 == 0:
            yield c
        a = b
        b = c

count = 0
for n in fibonacciGenerator(4000000):
    count += n

print count