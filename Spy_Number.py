n=int(input())
mul=1
sum=0
while(n>0):
    d=n%10
    sum=sum+d
    mul=mul*d
    n=n//10
if(mul==sum):
    print("Spy Number")
else:
    print("Not Spy Number")