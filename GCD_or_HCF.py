n1,n2=map(int,input().split())
for i in range(1,n1+1)and range(1,n2+1):
    if(n1%i==0 and n2%i==0):
        gcd=i
print(gcd)