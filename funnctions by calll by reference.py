def add(a):##formal parameters
    a+=[2,3]
    return a
a=list(map(int,input().split()))
print(add(a))##call by  reference,actual parameters
