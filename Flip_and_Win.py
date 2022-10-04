n=int(input())
s=input()
c=0
for i in range(1,n):
    c+=abs(int(s[i])-int(s[i-1]))
c=n-c-1
#print(c)
if(c%3==0):
    print("Sudhir")
else:
    print("Ashok")
    