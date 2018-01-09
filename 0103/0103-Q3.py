def main():
    times = eval(input())
    for i in range(times):
        text = input().split()
        s1 = ""
        s2 = ""
        for k in range(2):
            for j in range(len(text[k])):
                if text[k][j].isdigit():
                    s2 += text[k][j]
                else:
                    s1 += text[k][j]
        total = 0
        for each in s2:
            total += eval(each)
        s3 = total % 9
        print(s1 + s2 + str(s3))
main()
