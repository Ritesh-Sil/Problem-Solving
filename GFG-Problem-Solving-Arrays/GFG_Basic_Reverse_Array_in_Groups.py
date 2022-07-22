# Reverse array in groups
# Given an array arr[] of positive integers of size N.
# Reverse every sub-array group of size K.
#
# Input:
# N = 5, K = 3
# arr[] = {1,2,3,4,5}
# Output: 3 2 1 5 4
# Explanation: First group consists of elements
# 1, 2, 3. Second group consists of 4,5.

source = [1,2,3,4,5,6,7,8,9,10]
k = 3
index = k-1

target = []
while(index>=0): #2
    target.append(source[index]) #3 2 1
    source.remove(source[index]) #[4,5]
    index-=1 #1,0,-1
    #print(index)
    if index<0 and len(source)!=0 :
        if len(source)>=k:
            index = k-1
        else:
            index = len(source)-1

print(target)




