n=input().split(" ")
k=[]
for i in n:
    k.append(i)
#print(k)
l=1
for i in k:
    #print(i)
    if(i[0] in 'AEIOUaeiou'):
        i+='ma'+(l*'a')
        l+=1
    else:
        i=i[1:]+i[0]
        i+='ma'+(l*'a')
        l+=1
    print(i,end=" ")
