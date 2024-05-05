def is_prime(a):
    for i in range(2,int(a**0.5)+1):
        if(a%i==0):
            return 0
    else:
        return 1
def rev(m):
    s=0;
    while(m!=0):
        r=m%10
        s=s*10+r
        m=m//10
    return s
n=int(input())
s=0
if(is_prime(n)==1):
   
    if(is_prime(rev(n))==1): 
        print("Twisted prime")
    else:
        print("Not a twisted prime")
else:
    print("the given no is not a prime")
