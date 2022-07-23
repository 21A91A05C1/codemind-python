n=int(input())
p=list(map(int,input().split()))
k=int(input())
c=0
for i in p:
    if c<i:
        c=i
    if i+k>=c:
        print("True",end=" ")
    else:
        print("False",end=" ")
