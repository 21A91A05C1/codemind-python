n=int(input())
while(n!=0):
    k=int(input())
    i=1
    mul=1
    for i in range(1,k+1):
        mul=mul*i
    print(mul)
    n=n-1
    