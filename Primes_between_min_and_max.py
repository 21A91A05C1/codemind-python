def primes(n):
    d=0
    for i in range(1,n+1):
        if(n%i==0):
            d+=1
    if(d==2):
        return 1
    return 0

n=int(input())
k=list(map(int,input().split()))
p=min(k)
p1=k.index(p)
q=max(k)
q1=k.index(q)
if(q1<p1):
    q1,p1=p1,q1
c=0
for i in range(p1,q1+1):
    if(primes(k[i])):
        #print(k[i])
        c+=1
print(c)