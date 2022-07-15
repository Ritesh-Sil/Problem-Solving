# Write a program to find out the value of x raised to the power y , where x and y are positive integers

x = -4
y = 3

ans = 1
if x >0 and y>0:
    for i in range(3):
        ans =ans*x
    print(ans)

else:
    print("Invalid X or Y or both")


