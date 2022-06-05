s=input()
k=[]
for i in range(0,len(s)):
    flag=0
    for j in range(0,len(s)):
        if(s[i]==s[j] and i!=j):
            flag=1
            break
    else:
        k.append(s[i])
        print(*k)
        break
if(len(k)==0):
    print("-1")