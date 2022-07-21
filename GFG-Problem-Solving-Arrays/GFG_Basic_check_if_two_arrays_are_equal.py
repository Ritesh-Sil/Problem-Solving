#Check if two arrays are equal or not
# Input:
# N = 5
# A[] = {1,2,5,4,0}
# B[] = {2,4,5,0,1}
# Output: 1
# Explanation: Both the array can be
# rearranged to {0,1,2,4,5}

A = [1,2,5,4,0,3]
B = [2,4,5,0,1,3]

_dictA = {}
_dictB = {}

if len(A) != len(B):
    print("Arrays are not equal")
else:
    for i in range(len(A)):
        if A[i] not in _dictA.keys():
            _dictA[A[i]] = 1
        else:
            _dictA[A[i]]+=1

    for i in range(len(B)):
        if B[i] not in _dictB.keys():
            _dictB[B[i]] = 1
        else:
            _dictB[B[i]]+=1

    size = len(_dictB)

    for i in _dictA.keys():
        if _dictA[i] != _dictB[i]:
            flag = 0
            print("Not Same")
            break
        else:
            flag = 1

    if flag ==1:
        print("Same Arrays!")



