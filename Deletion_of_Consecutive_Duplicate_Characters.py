t=int(input())
while(t!=0):
    s=input()
    c=0
    for i in range(len(s)-1):
        if(s[i]==s[i+1]):
            c+=1
    print(c)
    t-=1