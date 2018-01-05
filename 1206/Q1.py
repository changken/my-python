'''
2017.12.06 Q1
尚未完成，蝸牛的天數感覺不對
'''
from sys import stdin

for row in stdin:
    row = row.replace("\n","")
    row = [eval(x) for x in row.split()]
    a, b, c, d = row[0], row[1], row[2], row[3]
    total = b
    count = 0
    while total < a:
        tmp = c - d
        total += tmp
        count += 1
    print(count)
