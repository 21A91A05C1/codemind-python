t=int(input())
n=list(map(int,input().split()))
c=0
if n[0]>n[1]:
    for i in range(len(n)-1):
        if i%2==0 and n[i]>n[i+1]:
            c+=1
        elif i%2==1 and n[i]<n[i+1]:
            c+=1
    if(c==t-1):
        print("yes")
    else:
        print("no")
            
else:
    for i in range(len(n)-1):
        if i%2==1 and n[i]>n[i+1]:
            c+=1
        elif i%2==0 and n[i]<n[i+1]:
            c+=1
    if(c==t-1):
        print("yes")
    else:
        print("no")
    
    