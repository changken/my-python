def main():
    leave = [[10, 1], [20, 2], [15, 3]]
    
    times = eval(input())
    for k in range(times):
        n = [eval(x) for x in input().split()] 
        if n[1] == 1:
            leave[n[0] - 1][0] += n[2] 
        elif n[1] == 2:
            leave[n[0] - 1][0] -= n[2]
    leave.sort()
    for i in range(len(leave)):
        print(leave[i][1], leave[i][0])
main()
