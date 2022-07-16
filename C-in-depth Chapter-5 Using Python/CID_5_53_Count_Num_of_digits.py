def num_of_digits_for(num):
    count = 0
    for i in range(len(str(num))):
        if num//10 !=0:
            count+=1
    print(count)

def num_of_digits_while(num):
    count = 0
    i=0
    while(i<len(str(num))):
        if num//10 !=0:
            count+=1
            i+=1
    print(count)
while(1):
    num = int(input("Please enter the num : ").strip())
    if num in [i for i in range(10)]:
        print(1)
    else:
        #num_of_digits_for(num)
        num_of_digits_while(num)
