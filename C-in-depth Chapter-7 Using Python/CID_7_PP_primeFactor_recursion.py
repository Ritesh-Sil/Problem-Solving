#Recursion : Perform prime factorization

def prime_factor(num):
    i=2
    if num == 1:
        return
    while(num%i != 0):
        i+=1
    print(i)
    prime_factor(num//i)


prime_factor(45)
