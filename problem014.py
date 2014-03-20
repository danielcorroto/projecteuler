'''
Created on Mar 19, 2014

@author: Daniel Corroto


The following iterative sequence is defined for the set of positive integers:
n -> n/2 (n is even)
n -> 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def transform(x):
    if x % 2 == 0:
        return x / 2
    else:
        return 3 * x + 1

def longestChain(x):
    num = 0
    length = 0
    for i in range(x):
        count = 1
        x = i
        while x > 1:
            x = transform(x)
            count += 1
        if count > length:
            num = i
            length = count
    return num

print longestChain(1000000)
