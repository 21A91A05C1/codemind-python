n=int(input())
c=0
z=0
r=0
for i in range(1,n+1):
    if(n%i==0):
        c=c+1
if(c==2):
    while(n>0):
        d=n%10
        r=r*10+d
        n=n//10
for j in range(1,r+1):
    if(r%j==0):
        z=z+1
if(c==2 and z==2):
    print("circular prime")
if(c==2 and z!=2):
    print("prime but not a circular prime")
elif(c!=2):
    print("not prime")