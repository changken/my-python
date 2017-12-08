k = eval(input())
for i in range(k):
    n = input()
    n = n.split()
    n = [eval(a) for a in n]
    Thismax = max(n)
    count = [0] * (Thismax + 1)
    for p in n:
        count[p] += 1
    Max = max(count)
    Many = count.index(Max)
    print(Many,Max)