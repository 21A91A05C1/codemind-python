t=int(input())
while(t>0):
    n=input()
    if(n==n[::-1]):
        if(len(n)%2==0):
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")
    t=t-1