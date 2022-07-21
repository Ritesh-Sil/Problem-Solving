A = [1, 7, 4, 3, 4, 8, 7]
size = len(A)

def first_repeated_elements(A):
    _list = []
    for i in range(size-1):
        if A[i] !=A[i+1]:
            _list.append(A[i])

        #print(_list)
        if A[i+1] in _list:
            value = A[i+1]
            break
    return value


print(first_repeated_elements(A))
