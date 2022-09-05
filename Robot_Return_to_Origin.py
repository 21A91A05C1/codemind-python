n=input()
#print(n)
u=d=l=r=0
for i in n:
    if i=='U':
        u+=1
    elif i=='D':
        d+=1
    elif i=='L':
        l+=1
    elif i=='R':
        r+=1
#print(u,d,l,r)
if(l==r and u==d):
    print("True")
else:
    print("False")