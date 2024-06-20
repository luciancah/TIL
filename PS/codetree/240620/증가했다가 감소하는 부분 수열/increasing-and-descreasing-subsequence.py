n = int(input())
nums = list(map(int, input().split()))
dp1 = [1] * n
dp2 = [1] * n

# dp 배열 : 나를 포함한 최대의 수열 길이

for i in range(n):
    flag = False
    for j in range(0, i):
        if nums[i] > nums[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

for i in range(n-1, -1, -1):
    flag = False
    for j in range(n-1, i, -1):
        if nums[i] > nums[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

max_dp = max(max(dp1), max(dp2))
for i in range(n):
    d1 = dp1[i]
    d2 = dp2[i]

    if d1 + d2 - 1 > max_dp:
        max_dp = d1 + d2 - 1

# print(dp1)
# print(dp2)
print(max_dp)