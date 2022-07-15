num  = 455567778
length = len(str(num))
digit = 7
count = 0
for i in range(length):
    res = num%10
    if res == digit:
        count+=1
    num = num//10

print(count)

