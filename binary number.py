def binary(n):
    k=0
    s=' '
    while n>0:
        l=n%2
        s+=str(l)
        k=n//2
        n=k
    
    return s[: :-1]
n=int(input())
for i in range(0,2*n):
    if i==0:
        print("000")
    else:
        print(binary(i))
##print(binary(n))
