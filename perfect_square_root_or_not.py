n=int(input())
c=0
for i in range(1,n):
    if(n==i*i):
        c=c+1
if(c>0):
    print("True")
else:
    print("False")
    