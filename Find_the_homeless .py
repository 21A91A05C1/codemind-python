n=int(input())
p=[]
f=n
h=[]
while(n!=0):
    k=int(input())
    p.append(k)
    n-=1
while(f!=0):
    l=int(input())
    h.append(l)
    f-=1
#print(p)
#print(h)
for i in p:
    for j in h:
        if i<=j:
            h.remove(j)
print(len(h))