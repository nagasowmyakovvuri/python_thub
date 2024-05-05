def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    else:
        return 1
n=int(input())
k=is_prime(n)
if k==1:
    print("True")
else:
    print("False")n
