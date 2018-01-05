from sys import stdin

for row in stdin:
    row = row.replace("\n","")
    row = int(row)
    count10 = row // 10
    row %= 10
    count5 = row // 5
    row %= 5
    count1 = row // 1
    row %= 1
    print("NT10=%d\nNT5=%d\nNT1=%d"%(count10, count5, count1))
