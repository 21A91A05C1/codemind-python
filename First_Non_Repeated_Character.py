t=int(input())
while(t>0):
    n=int(input())
    flag=0
    s=input()
    k=[]
    for i in range(len(s)):
        flag=0
        for j in range(len(s)):
            if s[i]==s[j] and i!=j:
                flag=1
                break
        if(flag==0):
            
            k.append(s[i])
            break
    if(len(k)!=0):
        print(*k)
    else:
        print("-1")
    t=t-1