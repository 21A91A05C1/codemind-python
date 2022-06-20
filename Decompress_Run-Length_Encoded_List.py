n=int(input())
nums=list(map(int,input().split()))
ans = []
for i in range(0, len(nums), 2):#  0  2
      ans+=[nums[i + 1]] * nums[i]  
print(*ans)