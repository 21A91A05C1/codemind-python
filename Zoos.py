n=input()
x=0
y=0
for i in n:
    if(i=='z'):
        x=x+1
    else:
        y=y+1
if(y==2*x):
    print("Yes")
else:
    print("No")