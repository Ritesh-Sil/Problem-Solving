num = 1000

for i in range(num):
    cube = i*i*i
    if cube%3 == 0 and cube<=num:
        print(cube)