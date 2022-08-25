n=int(input())
k=list(map(int,input().split()))
l=[]
for i in range(0,len(k)):
    for j in range(i+1,len(k)):
        if(k[i]<k[j]):
            l.append(j-i)
            break
    else:
        l.append(i-i)
print(*l)
            