n=int(input())
m=int(input())
c=0
for i in range(n,m+1):
    c=0
    if(i==1):
        continue
    for j in range(2,i):
        if(i%j==0):
            c=c+1
    if(c==0):
        print(i)