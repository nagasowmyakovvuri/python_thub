def is_prime(a):
    for i in range(2,int(n**0.5)+1):
        if a%i==0:
            return ("False")
    return ("True")
n=int(input())
k=is_prime(n)
print(is_prime(n))
print(k)
