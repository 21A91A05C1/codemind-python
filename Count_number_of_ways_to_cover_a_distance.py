n=int(input())
if(n<=2):
    print(n)
else:
    a=1
    b=1
    c=2
    r=0
    for i in range(3,n+1):
        r=a+b+c
        a=b
        b=c
        c=r
    print(r)
    