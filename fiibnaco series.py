##def fibnaco(n):
##    a=0
##    b=1
##    print(a,b,end=' ')
##    for i in range(n,4,-1):#5
##        c=a+b#1 2 3
##        print(c,end=' ')
##        a=b#1 1 2
##        b=c#1 2
def fibnaco(n):
    a=0
    b=1
    for i in range(2,n):
        c=a+b
        if c>n:
           return b
        a,b=b,c
n=int(input())
print(fibnaco(n))
##def fibnaco(n):
##    a=0
##    b=1
##    i=3
##    while("true"):
##        c=a+b
##        a,b=b,c
##        print(i)
##        if b==n:
##            print(i)
##            break
##        i=i+1
##        
##n=int(input())
##fibnaco(n)
