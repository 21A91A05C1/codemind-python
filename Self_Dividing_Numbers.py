def s(n):
    x=n
    c=0
    y=0
    while(n!=0):
        d=n%10
        if(d==0):
            return 0
        elif(x%d==0):
            c+=1
        y+=1
        n=n//10
    if(y==c):
        return 1
    return 0
    
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(s(i)==1):
        print(i,end=" ")