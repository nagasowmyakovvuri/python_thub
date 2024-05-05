n=int(input())
for i in range(n,0,-1):
    while j!=0:
        if j==n or j==1:
            print(i,end=' ')
        n=n-1
        j=j+1
        
    print()
