n=int(input())
arr=list(map(int,input().split()))
k=[]
c=0
for i in range(len(arr)):
    if(arr[i]==1):
        c+=1
    else:
        k.append(c)
        c=0
k.append(c)
print(max(k))