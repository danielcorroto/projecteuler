'''
Created on Mar 23, 2014

@author: Daniel Corroto

The nth term of the sequence of triangle numbers is given by, t_n = 1/2*n(n+1); so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t_10. If the word value is a triangle number then we shall call the word a triangle word.
Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''
from math import sqrt

'''
1/2*n*(n+1) = t
n^2 + n + 2t = 0
n = (-1+-sqrt(1+8t))/2
it's a triangle word if sqrt(1+8t) is int
'''

f = open("files/words.txt");
s = f.read()
f.close()
l = map(lambda x: x.replace("\"", ""), s.split(","))

count = 0
for word in l:
    value = sum([ord(i) - 64 for i in word])
    sqrtv = sqrt(1 + 8 * value)
    if int(sqrtv) * int(sqrtv) == sqrtv * sqrtv:
        count += 1

print count
