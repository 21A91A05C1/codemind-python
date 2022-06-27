n=int(input())
m=int(input())
c=2
z=0
res=n+m
for i in range(1,10):
    res1=res+i
    for j in range(2,res1):
        if(res1%j==0):
            c=c+1
            break
    else:
        print(i) 
        break