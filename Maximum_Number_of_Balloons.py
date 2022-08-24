n=input().lower()
c=0
d=0
a=0
b=0
k=0
ans=0
for i in n:
    if(i=="b"):
        c+=1
    elif(i=="a"):
        d+=1
    elif(i=="l"):
        a+=1
    elif(i=="o"):
        b+=1
    elif(i=="n"):
        k+=1
    
while(c!=0 and d!=0 and a!=1 and b!=1 and k!=0):
    c=c-1
    d=d-1
    a=a-2
    b=b-2
    k=k-1
    if(a<0 or b<0):
         break
    ans+=1
print(ans)
    