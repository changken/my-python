#助教版 已翻成Python
def main():
    n = eval(input())#int
    while n != 0:
        yes = False #Boolean
        i = 1
        j = 1
        while i <= n: #i小於等於n
            if (i ** 3) > n: #如果i^3大於n，必然的，不然減出來的值會是小於n
                while j < i: #j小於i，這是必然的，不然得出來的值會是負的(等於不用玩)
                    if (i ** 3 - j ** 3) == n: #如果i^3 - j^3等於n
                        yes = True #yes等於真
                        break #跳出第二層迴圈
                    j += 1
            if yes: #如果yes等於真
                break #跳出第一層迴圈
            i += 1
        if yes: #如果yes等於真
            print(i, j)#顯示其值
        else:
            print("No solution")
        n = eval(input())#int
    
main()
