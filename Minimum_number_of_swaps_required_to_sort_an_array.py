n=int(input())
arr=list(map(int,input().split()))
k=arr
k=sorted(k)
#print(arr)
#print(k)
c=0
for i in range(len(arr)):
    if arr[i]!=k[i]:
        c+=1
    c1=arr.index(k[i])
    arr[i],arr[c1]=arr[c1],arr[i]
print(c)