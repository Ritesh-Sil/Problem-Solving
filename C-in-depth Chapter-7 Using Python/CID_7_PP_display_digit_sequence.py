# Recursion : Display an integer as a sequence of characters
# return is must in recursion

def display_int(num):
    if num // 10 ==0:
        print(num)
        return
    else:
        rem = num % 10
        display_int(num//10)
        print(rem)



display_int(5432)