'''
Created on Mar 19, 2014

@author: Daniel Corroto

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 * 53 = 49714.
What is the total of all the name scores in the file?
'''

def worth(s):
    count = 0
    for i in s:
        count += ord(i) - 64
    return count

f = open("files/names.txt");
s = f.read()
f.close()
l = map(lambda x: x.replace("\"", ""), s.split(","))
l.sort()

count = 1
score = 0
for i in l:
    score += count * worth(i)
    count += 1

print score
