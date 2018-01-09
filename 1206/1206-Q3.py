from sys import stdin

for row in stdin:
    row = row.replace("\n", "")
    row = row.split("@")
    print("{0:s}, {1:s}".format(row[0], row[1]))
