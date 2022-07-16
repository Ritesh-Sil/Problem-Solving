# Write a progarm to enter a number and test if its fibonacci or not
#0,1,1,2,3,5


def fib_list():
    x = 0
    y = 1
    fib_list = []
    for i in range(0,num):
        z = x + y
        fib_list.append(z)
        x = y
        y = z
    return fib_list

while(1):
    num  = int(input("Enter the number : "))
    if num in fib_list():
        print(num , " : is a Fibonacci number")
    else:
        print("Not a fibonacci num")



