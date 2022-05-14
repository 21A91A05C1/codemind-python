n=int(input())
d=[]
c=0
flag=0
while(n>0):
    d.append(n%10)
    n=n//10
    c+=1
for i in range(0,c):
    for j in range(0,c):
        if(d[i]==d[j] and i!=j):
            flag=1
            break
    if(flag==1):
        print("Not Unique Number")
        break
      #  return 0
if(flag==0):
    print("Unique Number")
   # return 0