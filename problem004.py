#!/usr/bin/python
'''
Created on Mar 18, 2014

@author: Daniel Corroto

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

from numberUtil import isPalindrome

maxi = 0

a = 999
while a >= 100:
    b = 999
    while b >= 100:
        c = a * b
        if (c > maxi and isPalindrome(c)):
            maxi = c
        b -= 1
    a -= 1

print maxi
