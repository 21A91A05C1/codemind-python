n=int(input())
c=1
if(n<3 or n>100):
    print("The pattern is not possible")
else:
    for i in range(1,n*2):
        for j in range(1,c+1):
            print("*",end="")
        if(i<n):
            c=c+1
        else:
            c=c-1
        print()