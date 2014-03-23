'''
Created on Mar 23, 2014

@author: Daniel Corroto

An irrational decimal fraction is created by concatenating the positive integers:
0.12345678910*1*112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part, find the value of the following expression.
d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
'''

f = (1, 10, 100, 1000, 10000, 100000, 1000000)
res = 1
i = 1
index = 0
chars = 0
while i < 1000008:
    length = len(str(i))
    if index < len(f) and chars < f[index] and chars + length >= f[index]:
        res *= int(str(i)[f[index] - chars - 1])
        index += 1
    i += 1
    chars += length

print res
