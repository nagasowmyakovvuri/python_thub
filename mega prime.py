n=int(input())
flag=0
s=0
k=0
p=0
for i in range(2,(n//2)+1):
    if n%i==0:
        flag=1
        break
##print(flag)
while n!=0:
    r=n%10
    s=s+1
    ##print(s)
    p=0
    for i in range(2,(r//2)+1):
        if r%i==0:
            p=1
            break
    if p==0:
        k=k+1
    n=n//10
##print(k)
if k==s and flag==0:
    print("mega prime")
else:
    print("not a mega prime")
