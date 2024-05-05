a=int(input())
b=int(input())
p=0
##for i in range(a,b+1):
##     if i%2==0 and i%3==0:
##         print("yes")
##     else:
##         print("No")
for i in range(a,b+1):
     if i%2==0 and i%3==0:
         p+=1
print(p)
