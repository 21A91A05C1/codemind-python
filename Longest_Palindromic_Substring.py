def pal(s):
    if s==(s[::-1]):
        return 1
    else:
        return 0
n=input()
k=[]
s=''
for i in range(len(n)):
    s=''
    for j in range(i,len(n)):
        s=s+n[j]
        #print(s)
    #print(s)
    #print((s[::-1]))
        if(pal(s)):
            k.append(s)
k=sorted(set(k))
#print(k)
max=0
for i in k:
    if len(i)>max:
        max=len(i)
        p=i
print(p)