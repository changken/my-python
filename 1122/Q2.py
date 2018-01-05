import math

def main():
    while True:
        result = decrypt(input())
        if result != "END_TEST!":
            print(result)
        else:
            print(result)
            break

def decrypt(encrypt):
    
    Enlength = len(encrypt)
    Ensqrt = math.sqrt(Enlength)
    
    if math.ceil(Ensqrt) == Ensqrt:
        
        Ensqrt = int(Ensqrt)

        tmp = []
        word = ""

        c = 0
        for i in range(Ensqrt):
            tmp.append([])
            for j in range(c, c + Ensqrt):
                tmp[i].append(encrypt[j])
            c = j + 1

        for col in range(Ensqrt):
            for row in range(Ensqrt):
                word += tmp[row][col]

        return word 
    else:
        return "INVALID"

main()
