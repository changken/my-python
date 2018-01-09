import math

n = eval(input())

way = math.ceil(n / 2)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == way and j == way:
            print("$",end="")
        else:
            print("*",end="")
    print() 
