# Write a function that inputs a number and prints the multiplication table of that number

num = 8

def mult_table(num):
    for i in range(1,11):
        print(f"{num} x {i} = ", num*i)


mult_table(num)