n=int(input())
k=list(map(int,input().split()))
c=0
d=0
for i in range(len(k)-1,1,-1):
    if(k[i]==k[i-1]+k[i-2]):
        c+=1
    else:
        d=1
        break
if(c!=0 and d==0):
    print("yes")
else:
    print("no")
        