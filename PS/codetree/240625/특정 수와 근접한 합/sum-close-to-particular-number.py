n, s = map(int, input().split())
nums = list(map(int, input().split()))

diff = 9999999
sum_nums = sum(nums)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        ans = sum_nums - nums[i] - nums[j]
        diff = min(diff, abs(s - ans))

print(diff)