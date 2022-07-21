array = [1,7,3,4,2,9]
sum =14
def sumSubarray(array,sum):
    size = len(array) #6
    #print(size)
    sum_test = 0
    index = [1]
    j=0
    while(j<size):
        for i in range(size):
            sum_test +=array[j]
            if sum_test == sum:
                index.append(i+1)
                print(index)
        j+=1

sumSubarray(array,sum)

