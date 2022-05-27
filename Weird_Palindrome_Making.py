t=int(input())
while(t!=0):
    a=int(int(input()))
    b=list(map(int,input().split()))
    c=0
    for i in b:
        if i%2==1:
            c+=1 
    print(int(c/2))
    t-=1