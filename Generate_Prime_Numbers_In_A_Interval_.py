m = int(input())
n= int(input())
for i in range(m,n + 1):
   # all prime numbers are greater than 1
   if i > 1:
       for j in range(2,i):
           if (i % j) == 0:
               break
       else:
           print(i)