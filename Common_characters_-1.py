n=input().lower().split(" ")
c=0
d=0
p=n[0]
k=""
for i in p:
    c=0
    for j in range(1,len(n)):
        if i in n[j]:
            c+=1
            
    if(c==len(n)-1):
        d+=1
        k=k+i
if(len(k)!=0):
    print(k)
else:
    print("-1")