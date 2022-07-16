#Recursion :  Write a program to perform sum of digits

def sum_of_digits(num):
    if num//10 ==0:
        return num
    else:
        rem = num%10
        return rem + sum_of_digits(num//10)

print(sum_of_digits(5432))