def rev(m):
    s=0;
    while(m!=0):
        r=m%10
        s=s*10+r
        m=m//10
    return s
m=int(input())
res=rev(m)
print(res)
