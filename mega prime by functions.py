def is_prime(a):
    for i in range(2,int(a**0.5)+1):
        if(a%i==0):
            return 0
    else:
        return 1
    


n=int(input())

##print(h)
k=0
l=0
if(is_prime(n)==1):
    while n!=0:
       r=n%10
       k=k+1
    ##]print(k)
    ##is_prime(r)
       if(is_prime(r)==1):
          l=l+1
       n=n//10
    ##print(l ,k)
    if(l==k):
       print("mega prime")
    else:
      print("not a mega prime")
else:
    print("not a prime")


