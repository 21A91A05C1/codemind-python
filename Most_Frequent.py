n=int(input())
k=list(map(int,input().split()))
c=l=m=0
for i in range(0,len(k)):
    c=1
    for j in range(0,len(k)):
        if i!=j:
            if(k[i]==k[j]):
                c+=1
    if(c>l):
        l=c
        m=k[i]
    elif(c==l):#hidden failed 
    #as when two numbers has same frequency we shold return 
    #smaller number so
        l=c
        if(k[i]<m):
            m=k[i]
    
print(m)    