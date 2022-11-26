n=int(input())
arr=list(map(int,input().split()))
c=0
o=0
for i in arr:
    if(i%2==0):
        c+=1
    else:
        o+=1
if(c==o or c%2==0):
    print("1")
else:
    print("0")