# Write a program that inputs an integer n and displayes nxn checkerboard pattern

num = 8

for i in range(num):
    if i%2 ==0:
        print("* "*(num))
    else:
        print(" *"*(num))