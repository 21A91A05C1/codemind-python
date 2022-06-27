n=input()
k=[]
for i in range (len(n)):
    flag=0
    for j in range(len(n)):
        if (n[i]==n[j] and i!=j):
            flag=1
            break
    else:
        k.append(n[i])
        print(*k) 
        break;
if(flag==1):
    print("-1")
        