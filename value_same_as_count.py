n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    b=l.count(i)
    if(b==i):
        c+=1
        if(b>1):
            l.remove(i)

print(c)