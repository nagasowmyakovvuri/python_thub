##a=list(map(str,input().split()))
##b=list(map(str,input().split()))
##f=0
##for i in a:
##        if i not in b:
##            f+=ord(i)
##for j in b:
##    if j not in a:
##        f+=ord(j)
##k=f
##while(k>=10):
##    s=0
##    while f!=0:
##        r=f%10
##        s+=r
##        f=f//10
##    f=s
##    k=s
##print(s)
