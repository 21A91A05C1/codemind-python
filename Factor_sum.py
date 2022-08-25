l=list(map(int,input().split(',')))
p=[]
for i in l:
    s=0
    for j in range(1,i+1):
        if i%j==0:
            s=s+j
    if s in l:
        p.append(i)
if(len(p)!=0):
    print(*sorted(p))
else:
    print("-1")