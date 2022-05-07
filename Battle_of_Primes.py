n=int(input())
m=int(input())
r=n+m
for i in range(1,11):
    s2=r+i
    for j in range(2,s2):
        if(s2%j==0):
            break
    else:
        print(i)
        break
        