n=int(input())
def fun( n):
    r=0
    while(n):
        d=n%10
        r=r*10+d
        n=n//10
    return r
while(n):
    n=n+fun(n)
    if(n==fun(n)):
        print(n)
        break
    