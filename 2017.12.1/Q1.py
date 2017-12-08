from sys import stdin
for row in stdin:
    for i in range(len(row)):
        if i == 0:
            ans = eval(row[i])
        elif row[i] == "\n":
            j = 0
        else:
            ans *= eval(row[i])
    print(ans)