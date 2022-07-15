# Write a program to check whether a number is palindromic or not
# How to reverse a number

def rev_num(num):
    sum = 0
    res = 0
    for i in range(len(str(num))+1):
        sum = sum*10+res #0 #3 #34
        res = num%10    #3 #4 #2
        num = num//10 #24 #2 #0

    return sum

def is_4_digit_palindrome(num):
    if num == rev_num(num) and len(str(num))==4:
        print("4 digit Palindrome")
    else:
        print("Not 4 digit Palindrome")


while(1):
    num = int(input("Please enter the number: ").strip())
    is_4_digit_palindrome(num)





