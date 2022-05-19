n=input()
v=input()
for i in range(len(n)):
    if n[i]==v:
        print("True")
        print(i)
        break
else:
    print("False")