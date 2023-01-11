t=int(input())
while(t!=0):
    k=[]
    n=(input())
    for i in range(len(n)):
        k.append(int(n[i]))
    p=min(k)
    k.sort()
    for i in k:
        if(i!=p):
            print("NO")
            break
        else:
            p+=1
    else:
        print("YES")
    t-=1