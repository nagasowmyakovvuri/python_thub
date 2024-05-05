n=int(input())
i=1
k=1
while k<n*n+1:
    k=k+1
    print(i,end=' ')
    if i==n:
        i=0
        print()
    i=i+1
    ##print(k)
