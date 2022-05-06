n=int(input())
c=2
k=0
dc=0
z=0
for i in range(2,n):
    if(n%i==0):
        print("Not Mega Prime")
        break
else:
    while(n>0):
        k=0
        d=n%10
        for j in range(1,d+1):
            if(d%j==0):
                k=k+1
        dc=dc+1
        n=n//10
        if(k==2):
            z=z+1
    if(dc==z):
        print("Mega Prime")
    else:
        print("Not Mega Prime")