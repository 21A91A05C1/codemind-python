def pal(n):
    r=0
    temp=n
    while(n!=0):
        d=n%10
        r=r*10+d
        n=n//10
    if(temp==r):
        return 1
    return 0

n=int(input())
k=0
l=0
for i in range(n-100,n):
    if(pal(i)):
        k=i
for i in range(n+1,n+11):
    if(pal(i)):
        l=i
if(abs(n-k)<abs(l-n)):
    print(k)
elif(abs(n-k)==abs(l-n)):
    print(k,l)
else:
    print(l)