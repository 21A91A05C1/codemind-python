a=int(input())
b=int(input())
r=0
for i in range(a,b):
    n=i
    while(n):
        d=n%10
        r=r*10+d
        n=n//10
    if(r==i):
        print(i,end=" ")
    r=0
  