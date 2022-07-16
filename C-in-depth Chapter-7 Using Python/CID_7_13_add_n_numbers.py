

def sum_n_num(n):
    if n==0:
        return 0
    else:
        return n+sum_n_num(n-1)

print(sum_n_num(5))

