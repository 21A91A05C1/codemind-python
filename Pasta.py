n,m=map(int,input().split())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
c=0
for i in brr:
    if i in arr:
        arr.remove(i)
    else:
       c+=1
       break
if(c==0):
    print("Yes")
else:
    print("No")