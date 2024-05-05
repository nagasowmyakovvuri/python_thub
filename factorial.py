
##def factorial(a):
##    r=1
##    for i in range(n,0,-1):
##        r*=i
##    return r
def factorial(n):
    if n==1:##termination condition
        return 1
    return n*factorial(n-1)
n=int(input())
print(factorial(n))
