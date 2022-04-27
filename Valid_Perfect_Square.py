from math import sqrt
k=int(input())
for i in range(1,k+1):
    n = int(input())
    s=int(sqrt(n))
    if(s*s == n):
        print("True")
    else:
        print("False")