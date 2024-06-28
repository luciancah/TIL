n = int(input())
nums = list(map(int, input().split()))

res = []
ans = []
for i in range(len(nums)):
    res.append(nums[i])
    if i % 2 == 0:
        res.sort()
        ans.append(str(res[i//2]))

print(' '.join(ans))