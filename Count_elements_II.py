n,m=map(int,input().split())
l=list(map(int,input().split()))
z=list(map(int,input().split()))
l=set(l)
z=set(z)
c=0
for i in l:
    if i not in z:
        c=c+1
for i in z:
    if i not in l:
        c=c+1
print(c)