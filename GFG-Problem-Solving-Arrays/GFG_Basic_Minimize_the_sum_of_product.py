# You are given two arrays, A and B, of equal size N.
# The task is to find the minimum value of A[0] * B[0] + A[1] * B[1] + .... + A[N-1] * B[N-1],
# where shuffling of elements of arrays A and B is allowed.

#Input:
N = 5
# A = [6, 1, 9, 5, 4]
# B = [3, 4, 8, 2, 4]
# Output:
# 80
A = [6, 1, 9]
B = [3, 4, 8]

for i in range(len(A)):
    for j in range(len(B)):
        print(A[i],B[j])


