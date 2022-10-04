n=input()
l=0
m=len(n)
k=[]
for i in n:
    if i=="I":
        k.append(l)
        l+=1
    elif i=="D":
        k.append(m)
        m-=1
print(*k,end=" ")
print(l)