# CubeSum(), printArmstrong(), isArmstrong()

def cubesum(num):
    sum = 0
    length_num = len(str(num))
    for i in range(length_num):
        rem = num%10
        sum = sum+rem**3
        num = num//10
    return sum

def printArmstong(num):
    for i in range(1000):
       if num == cubesum(num):
           print(num)
