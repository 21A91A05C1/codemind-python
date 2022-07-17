n=int(input())
k=list(map(int,input().split()))
c=0
for i in range(1,len(k)-1,2):
    if k[i-1]<k[i]:
        c+=1
    else:
        c=0
        break
if(c!=0):
    print(c)
else:
    print("-1")