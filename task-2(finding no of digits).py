a,b=map(int,input().split())
import math
math.log10
####k=int(math.log10(a))+1
##o=str(a)
##k=len(o)
##print(k)
for i in range(a,b+1):
    l=int(math.log10(i))+1
    while i!=0:
        r=i%pow(10,l)
        print(r)
        i=i//pow(10,l)
        l=l-1
    print()
        
    
    
