n=int(input())
p=0
for i in range(1,n+1):
    p=0
    for j in range(i,n):
        print("@",end='')
        p=p+1
    for k in range(1,i+1):
        print("*",end='')

    
    print()
    print(p)
    
        
