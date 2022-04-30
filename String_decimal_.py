t=int(input())
while(t!=0):
    n=input()
    flag=0
    for i in n:
        if(i<'0' or i>'9'):
            flag=1
            break
    if(flag==1):
        print("False")
    else:
        print("True")
