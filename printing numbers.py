a=int(input())
b=int(input())
##for i in range(25,35+1):
##    print(i,end=' ')
    
##for i in range(a,-a-1,-1):
##    print(i,end=' ')
if a<b:
    for i in range(a,b+1):
        print(i,end=' ')
elif(a==b):
    print("no output")
else:
    for i in range(a,b-1,-1):
        print(i,end=' ')
