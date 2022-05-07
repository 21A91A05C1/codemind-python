n=int(input())
m=list(map(int,input().split()))
e=0
o=0
for i in range(len(m)):
    if i%2==0:
        e=e+m[i]
    else:
        o=o+m[i]
if(o-e==0):
    print("YES")
else:
    print("NO")
        