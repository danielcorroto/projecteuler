'''
Created on Mar 19, 2014

@author: Daniel Corroto

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

"""            1-9    11-99    100-999    1000    total    sum
one         3    1    8        100+9*9    1        191    573    573
two         3    1    8        100+9*9    0        190    570    1143
three       5    1    8        100+9*9    0        190    950    2093
four        4    1    8        100+9*9    0        190    760    2853
five        4    1    8        100+9*9    0        190    760    3613
six         3    1    8        100+9*9    0        190    570    4183
seven       5    1    8        100+9*9    0        190    950    5133
eight       5    1    8        100+9*9    0        190    950    6083
nine        4    1    8        100+9*9    0        190    760    6843
        190*(3*3 + 4*3 + 5*3) + 3 = 6843
ten         3   0     1        9        0        10        30
eleven      6    0    1        9        0        10        60
twelve      6    0    1        9        0        10        60
thirteen    8    0    1        9        0        10        80
fourteen    8    0    1        9        0        10        80
fifteen     7    0    1        9        0        10        70
sixteen     7    0    1        9        0        10        70
seventeen   9    0    1        9        0        10        90
eighteen    8    0    1        9        0        10        80
nineteen    8    0    1        9        0        10        80
        10*(3*1 + 6*2 + 7*1 + 8*5 + 9*1) 700
twenty      6    0    10    9*10        0        100        600
thirty      6    0    10    9*10        0        100        600
forty       5    0    10    9*10        0        100        500
fifty       5    0    10    9*10        0        100        500
sixty       5    0    10    9*10        0        100        500
seventy     7    0    10    9*10        0        100        700
eighty      6    0    10    9*10        0        100        600
ninety      6    0    10    9*10        0        100        600
        100*(6*4 + 5*3 + 7*1) = 4600
hundred     7    0    0    100*9        0        900        6300
and         3    0    0    99*9         0        891        2673
thousand    8    0    0    0            1        1            8
        6300+2673+8 = 8981
"""

def writeNumber(x):
    digit = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety", 100:"hundred"}
    if (x == 1000):
        return "one thousand"
    s = ""
    ''' hundreds'''
    part = x % 100
    if (x >= 100):
        s += digit[x // 100] + " " + digit[100]
        if part != 0:
            s += " and "

    if (part >= 20):
        s += digit[part // 10 * 10]
        if part % 10 > 0:
            s += "-" + digit[part % 10]
    elif (part > 0):
        s += digit[part]

    return s

count = 0
for i in range(1, 1001):
    count += len(writeNumber(i).replace(" ", "").replace("-", ""))
    print writeNumber(i), count

print count
