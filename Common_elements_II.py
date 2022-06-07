n,m=map(int,input().split())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
s=[]
for i in l:
    if i not in k:
        s.append(i)
for i in k:
    if i not in l:
        s.append(i)
print(*s)