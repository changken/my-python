def main():
    times = eval(input())
    for k in range(times):
        log = [eval(x) for x in input().split()]
        score = (log[0] * 1 + log[2] * 2 + log[1] * 2 + log[3] * 2) - (log[4] * 2)
        if score >= 45:
            print("A")
        elif score >= 35:
            print("B")
        elif score >= 25:
            print("C")
        else:
            print("D")
main()
