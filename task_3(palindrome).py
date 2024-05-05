a,b=map(int,input().split())
import math
for i in range(a,b+1):
    k=i
    r=0
    sum=0
    while i!=0:
        r=i%10
        sum=sum*10+r
        i=i//10
    if k==sum:
        print(k,"is palindrome")
##    else:
##        print(k,"is not a palindrome")

