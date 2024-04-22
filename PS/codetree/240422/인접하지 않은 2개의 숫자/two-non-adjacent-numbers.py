n = int(input())
nums = list(map(int, input().split()))

max_sum = 0
for i in range(len(nums) - 1):
    for j in range(i + 2, len(nums)):
        s = nums[i] + nums[j]
        max_sum = max(s, max_sum)

print(max_sum)