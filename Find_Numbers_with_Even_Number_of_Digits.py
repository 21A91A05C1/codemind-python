n=int(input())
m=list(map(int,input().split()))
f=0
for i in range(len(m)):
    c=0
    while(m[i]!=0):
        d=m[i]%10
        c+=1
        m[i]=m[i]//10
    if(c%2==0):
        f+=1
print(f)
        