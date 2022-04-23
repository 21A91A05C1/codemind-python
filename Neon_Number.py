n=int(input())
p=n*n
sum=0
while(p!=0):
    d=p%10
    sum=sum+d
    p=p//10
if(n==sum):
    print("Neon Number")
else:
    print("Not Neon Number")
