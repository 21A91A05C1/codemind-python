n=int(input())
l=list(map(int,input().split()))
k=[]
s=0
for i in l:
    if i not in k:
        k.append(i)
for j in k:
    if j%2==0:
        s=s+j
print(s)
    