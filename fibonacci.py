n=int(input())
a=0
b=1
for i in range(1,n+1):
    print(a,end=(" "))
    res=a+b
    a=b
    b=res
    