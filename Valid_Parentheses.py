def isValid(s):
    o = "{[("
    c = "}])"
    b= {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in o:
            stack.append(char)
        elif char in c:
            if len(stack) == 0:
                return False
            if stack[-1] == b[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0
t=int(input())
while(t>0):
    s=input()
    print(isValid(s))
    t=t-1