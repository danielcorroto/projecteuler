'''
Created on Mar 19, 2014

@author: Daniel Corroto

You are given the following information, but you may prefer to do some research for yourself.
    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

def isLeap(x):
    return (x % 4 == 0 and x % 100 != 0) or x % 400 == 0

def daysInMonth(y,m):
    if (m in [1,3,5,7,8,10,12]):
        return 31
    elif (m in [4,6,9,11]):
        return 30
    else:
        return 29 if(isLeap(y)) else 28

day = 1
count = 0
for y in range(1900,2001):
    for m in range(1,13):
        day = (day + daysInMonth(y, m)) % 7
        if (y > 1900 and day == 0):
            count += 1

print count