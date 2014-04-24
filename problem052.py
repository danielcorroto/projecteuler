'''
Created on Apr 24, 2014

@author: Daniel Corroto


It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

found = False
count = 0
while not found:
    count += 1
    if len(str(count)) == len(str(count * 6)):
        for i in range(2, 7):
            if not "".join(sorted(str(count))) == "".join(sorted(str(count * i))):
                break
            if i == 6:
                print count, count * 2, count * 3, count * 4, count * 5, count * 6
                found = True
