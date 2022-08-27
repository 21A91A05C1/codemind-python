def fun(n):
    r=""
    while(n>0):
        r=chr(ord('A')+(n-1)%26)+r
        n=(n-1)//26
    return r
n=int(input())
a=fun(n)
print(a)