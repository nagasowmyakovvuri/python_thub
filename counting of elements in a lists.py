a=list(map(int,input().split()))
d=[]
k=[]
c=0
for i in a:
    c=0
    for j in a:
        if i==j and i not in d:
            c=c+1
            d.append(i)
for i in d:
    c=0
    for j in a:
        if i==j:
            c=c+1
    k.append(c)
print(d)
print(k)
 
