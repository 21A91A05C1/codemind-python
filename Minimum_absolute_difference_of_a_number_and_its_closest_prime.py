def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if(c==2):
        return 1
    return 0
n=int(input())
min=999
for i in range(n-10,n+10):
    if(prime(i)):
        k=abs(n-i)
        if(k<min):
            max=k
print(min)
        