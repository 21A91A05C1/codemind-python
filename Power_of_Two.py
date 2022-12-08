n=int(input())
k=0
i=1
c=0
while(k<=n):
    k=2**i
    if(k==n):
        c+=1
        break
    i+=1
if(c!=0):
    print("True")
else:
    print("False")
        