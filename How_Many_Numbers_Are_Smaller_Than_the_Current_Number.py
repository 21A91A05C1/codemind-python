n=int(input())
m=list(map(int,input().split()))
c=0
for i in range(len(m)):
    c=0
    a=m[i]
    for j in range(len(m)):
        if(m[j]<a):
            c+=1
    print(c,end=" ")