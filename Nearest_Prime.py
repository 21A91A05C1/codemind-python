k=int(input())
while(k!=0):
    a=int(input())
    for n in range(a,1,-1):
        for i in range(2,int(a**0.5)+1):
            if(n%i==0):
                break
        else:
        #print(n,end=' ')
            break
    b=a
    while True:
        for i in range(2,int(a**0.5)+1):
            if(a%i==0):
                break
        else:
       # print(a,end=' ')
            break
        a=a+1
    if abs(b-n)>(abs(a-b)):
        print(a)
    else:
        print(n)
    k=k-1