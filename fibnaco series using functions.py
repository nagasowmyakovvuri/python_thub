def fibnaco(n):
    if(n<=1):
        return n
    return fibnaco(n-2)+fibnaco(n-1)
n=int(input())
for i in range(n):
    print(fibnaco(i),end=' ')

