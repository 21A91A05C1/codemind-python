n=int(input())
r=0
p=0
while(n>0):
    d=n%10
    r=r*10+d
    n=n//10
while(r>0):
    d1=r%10
    if(d1%2!=0):
        p=d1*d1
        print(p,end="")
    r=r//10