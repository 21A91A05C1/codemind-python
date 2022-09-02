t=int(input())
while(t!=0):
    n=int(input())
    l=list(map(int,input().split()))[1:]
    p=list(map(int,input().split()))[1:]
    k=[]
    #print(set(l))
    #print(set(p))
    for i in l:
        if i not in k:
            k.append(i)
    for i in p:
        if i not in k:
            k.append(i)
    #print(k)
    if len(k)==n:
        print("YES")
    else:
        print("NO")
    t-=1