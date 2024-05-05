def colatzsequence(n):
    s=n
    if(n%2!=0):
        s=3*n+1
    print(s,end=' ')
    while (1):
        k=s//2
        if(k==1):
            break
        print(k,end=' ')
        s=k
n=int(input())
colatzsequence(n)
