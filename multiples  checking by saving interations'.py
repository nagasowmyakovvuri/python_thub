n=int(input())
p=0
for i in range(6,n+1,6):
    p=p+1
    print(i,end=' ')
print()
print(p)
print()
p=0
for i in range(2,n+1,2):
    p=p+1
    if i%3==0:
        print(i,end=' ')
print()
print(p)
print()
p=0
for i in range(3,n+1,3):
    p=p+1
    if i%2==0:
        print(i,end=' ')
print()
print(p)
