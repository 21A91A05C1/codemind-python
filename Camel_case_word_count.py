a=input()
c=0
for i in range(1,len(a)):
    if(ord(a[i])>=65 and ord(a[i])<=90):
        c+=1
print(c+1)