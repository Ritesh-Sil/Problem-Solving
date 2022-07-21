# Given a sorted array of size N and an integer K, find the position at which K is present in the array using binary search.
# Input:
# N = 5
# arr[] = {1 2 3 4 5}
# K = 4
# Output: 3
# Explanation: 4 appears at index 3.
array = [1,2,3,4,5,6,8]
size = len(array)
# print(size)
start = 0
end = size-1
key = 1


def binarySearch(array, key, start, end):
    mid = (start+end)//2
    if array[mid] == key:
        return mid+1
    elif key > array[mid]:
        return binarySearch(array, key, mid+1, end)
    else:
        return binarySearch(array, key, start, mid-1)

print(binarySearch(array, key, start, end))