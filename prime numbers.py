n=int(input())
p=0
##method-1
##for i in range(1,n+1):
##    if n%i==0:
##        p=p+1
##if p==2:
##    print("prime")
##else:
##    print("not a prime")
##method-2
##for i in range(2,n):
##    if n%i==0:
##      print(" not a prime")
##      break
##else:
##    print("prime")
##method-3
##for i in range(2,(n//2)+1):
##    if n%i==0:
##      print(" not a prime")
##      break
##else:
##    print("prime")
##method-4
for i in range(2,int(n**0.5)+1):
    if n%i==0:
      print(" not a prime")
      break
else:
    print("prime")



