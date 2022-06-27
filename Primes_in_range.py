from math import sqrt
def is_prime(n):
    if n==1:
        return 0
    for i in range(2,int(sqrt(n))+1):
        if (n%i==0):
            return 0
    return 1
k=int(input())
p=int(input())
c=0
for i in range(k,p+1):
    if(is_prime(i)):
        c+=1
print(c)