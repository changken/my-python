def main():
    times = eval(input())
    for k in range(times):
        n = [eval(x) for x in input().split()]
        f = n[0] * (1 + (n[1] / 1200)) ** (12 * n[2])
        print("{0:.2f}".format(f))
main()
