n1=int(input())
k1=list(map(int,input().split()))
n2=int(input())
k2=list(map(int,input().split()))
l=[]
for i in range(len(k1)):
    l.insert(k2[i],k1[i])
print(*l)