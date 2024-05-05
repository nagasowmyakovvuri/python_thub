def lcm(a,b):
    max=maximum(a,b)
    while(1):
        if max%a==0 and max%b==0:
            return max
        max=max+1
def maximum(a,b):
    if a>b:
        return a
    return b
m,n=map(int ,input().split())
print(lcm(m,n))
