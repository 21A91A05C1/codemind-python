n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
p=[]
p=sorted(set(b))
for i in range(len(a)):
    for j in range(len(p)):
        if(a[i]==p[j] and a[i]!=-1):
            p[j]=-1;
            print(a[i],end=" ")