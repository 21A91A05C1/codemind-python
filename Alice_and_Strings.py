t=int(input())
while(t!=0):
    n=input()
    k=input()
    for i in range(len(n)):
        if(ord(n[i])>ord(k[i])):
            print("NO")
            break
    else:
        print("YES")
    t-=1