'''
Created on Mar 20, 2014

@author: Daniel Corroto

Take the number 192 and multiply it by each of 1, 2, and 3:
    192 * 1 = 192
    192 * 2 = 384
    192 * 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''
from numberUtil import isPandigital

maxi = 0
count = 0
for x in range(1, 1000):
    x = int("9" + str(x))
    temp = str(x)
    count = 2
    while len(temp) < 9:
        temp += str(int(x) * count)
        count += 1
    if len(temp) == 9 and int(temp) > maxi and isPandigital(int(temp)):
        maxi = int(temp)
        count = x

print count, maxi