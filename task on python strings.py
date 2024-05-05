a=input()
s=""
f=''
l=97
for i in range(1,27):
    if l<=123:
        f+=chr(l)
    l+=1
print(f)
k=0
h=0
i=0
c=0
for i in range(len(a)):
    if a[i]==":":
        c=c+1
        if(a[i-1]==a[i-2]):
            s+=chr(ord(a[i-1])-32)
         
        else:
            for j in range(len(f)):
                if(f[j]==max(a[i-1],a[i-2])):
                    k=j
                if f[j]==min(a[i-1],a[i-2]):
                    h=j
            m=k-h
            s+=chr(ord(f[max])-32)
    else:
        i=i+1
print(s)


##a=input()
##s=" "
##for i in range(0,len(a),3):
##    if a[i]==a[i+1]:
##        s+=chr(ord(a[i])-32)
##    else:
##        b=ord(max(a[i:i+2]))-ord(min(a[i:i+2]))
##        s+=chr(64+b)
##print(s)
##            
