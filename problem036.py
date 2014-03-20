'''
Created on Mar 20, 2014

@author: Daniel Corroto

The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

def reverseString(x):
    return "".join([x[i] for i in range(len(x) - 1, -1, -1)])

def decToBi(x):
    temp = ""
    while x > 0:
        temp = str(x % 2) + temp
        x //= 2
    return temp

def isPalindromicDecAndBi(x):
    if (x == reverseString(x)):
        b = decToBi(int(x))
        if (b == reverseString(b)):
            return True
    return False

temp = 0
for i in range(1, 1000):
    if i < 10 and isPalindromicDecAndBi(str(i)):
        temp += i
    if isPalindromicDecAndBi(str(i) + reverseString(str(i))):
        temp += int(str(i) + reverseString(str(i)))
    if i < 100:
        for j in range(10):
                if isPalindromicDecAndBi(str(i) + str(j) + reverseString(str(i))):
                    temp += int(str(i) + str(j) + reverseString(str(i)))

print temp
