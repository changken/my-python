def main():
    times = eval(input())
    for k in range(times):
        path = input()
        setting = input().split()

        if eval(setting[0]) == 1 and eval(setting[1]) == 2:
            path = path.replace(setting[2], setting[3])
            newPath = path.replace("\\","/")

        else:
            path = path.replace(setting[2], setting[3])
            newPath = path.replace("/","\\")
        print(newPath)
main()
