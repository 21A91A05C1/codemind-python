n=int(input())
while(sum!=1 and sum!=4):
    sum=0
    while(n>0):
        d=n%10
        sum=sum+d*d
        n=n//10
    n=sum
if(sum==1 or  sum==7):
    print("True")
else:
    print("False")