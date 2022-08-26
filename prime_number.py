n=int(input())
def fun(n):
    for i in range(2,n-1):
        if n%i==0:
            print("not a prime")
            break
    else:
        print("prime")
k=(fun(n))