n=int(input())
c=0
sq=n*n
temp=n
while(n>0):
    d=n%10
    n=n//10
    c=c+1
n=temp
p=10**c
k=sq%p
if(k==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")