#Given an array of N integers. Find the first element that occurs atleast K number of times.
# Input :
# N = 7, K = 2
# A[] = {1, 7, 4, 3, 4, 8, 7}
# Output :
# 4
# Explanation:
# Both 7 and 4 occur 2 times.
# But 4 is first that occurs 2 times.

A = [1, 7, 4, 3, 4, 8, 7]
k =2
_dict = {}
size = len(A)

for i in range(size):
    if A[i] not in _dict.keys():
        _dict[A[i]] = 1
    else:
        _dict[A[i]]+=1

    if _dict[A[i]] ==k:
        print(A[i])
        break
