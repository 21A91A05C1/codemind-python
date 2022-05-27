def fun(x, y):
    while(y):
        x, y = y, x % y
  
    return x
      
k=int(input())
l =list(map(int,input().split()))
  
num1=l[0]
num2=l[1]
gcd=fun(num1,num2)
  
for i in range(2,len(l)):
    gcd=fun(gcd,l[i])
      
print(gcd)