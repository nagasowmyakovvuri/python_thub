a=int(input())
b=int(input())
p=0
for i in range(a,b+1):
    k=i
    s=i
    count=0
    sum=0
    r=0
    while i!=0:
        count=count+1
        i=i//10
    while k!=0:
        r=k%10
        sum=sum+pow(r,count)
        k=k//10
    print(s," is amstrong")if sum==s else print(s,"is not amstrong")
##    print()
##    if s==sum:
##        p=p+1
##        print(s,end=' ')
##print(p)
