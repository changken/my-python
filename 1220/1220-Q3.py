def check(lst):
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            return False
    return True

def main():
    times = eval(input())
    for k in range(times):
        lst = [eval(x) for x in input().split()]
        if check(lst):
            print("Yes")
        else:
            print("No")
main()
