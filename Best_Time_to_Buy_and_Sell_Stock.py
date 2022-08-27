n=int(input())
k=list(map(int,input().split()))
l=[]
for i in range(len(k)):
    for j in range(i+1,len(k)):
        l.append(k[j]-k[i])
m=max(l)
if (m)>0:
    print(m)
else:
    print("0")
