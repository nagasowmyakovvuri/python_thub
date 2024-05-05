def deci(n):
    j=0
    s=0
    while(n!=0):
       r=n%10
       s=s+r*pow(2,j)
       n=n//10
       j=j+1
    return s
n=int(input())
print(deci(n))
