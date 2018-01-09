def main():
    while True:
        n = input().split()

        if n[0] == "0":
            break
        
        result = ""
        for k in range(len(n)):
            length = len(n[k])
            if length >= 3:
                result += n[k][2:] + n[k][:2]
            else:
                result += n[k]
            if k != (len(n) - 1):
                result += "-"
        print(result)
main()
