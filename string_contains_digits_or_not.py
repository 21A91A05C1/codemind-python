t=int(input())
while(t):
    n=input()
    c=0
    for i in n:
        if(i.isnumeric()):
            c=c+1
    if(c>0):
        print("Yes")
    else:
        print("No")
    t=t-1