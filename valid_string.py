n=input()
k=[]
for i in set(n):
    k.append(n.count(i))
#print(k)
max=max(k)
min=min(k)
c=0
d=0
for i in n:
    p=n.count(i)
    if(p==max):
        c+=1
    elif(p==min):
        d+=1
#print(c)
#print(d)
if(c==len(n) or d==len(n) or c==len(n)-1  or d==len(n)-1):
    print("Valid String")
else:
    print("Not Valid")
    