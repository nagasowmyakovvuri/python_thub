a=int(input())
b=int(input())
count=0
p=0
for i in range(a,b+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count=count+1
##            print(count)
    if count==2:
        p=p+1
####        print(p)
print(p)
