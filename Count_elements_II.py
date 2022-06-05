n,m=map(int,input().split())
l=list(map(int,input().split()))
p=list(map(int,input().split()))
l=set(l)
p=set(p)
c=0
for i in l:
    if i not in p:
        c+=1
for i in p:
    if i not in l:
        c+=1
print(c)
