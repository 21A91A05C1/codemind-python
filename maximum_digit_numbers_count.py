n=int(input())
l=list(map(int,input().split()))
max=0
for i in range(len(l)):
    if len(str(l[i]))>max:
        max=len(str(l[i]))
for i in range(len(l)):
    if len(str(l[i]))==max:
        print(l[i],end=" ")
