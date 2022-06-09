l=list(map(str,input().split()))
for i in l:
    k=min(i)
    p=max(i)
    #print(k)
    #print(p)
    w=abs(ord(k)-ord(p))
    print(w,end=" ")