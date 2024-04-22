n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))

nums += nums

min_dist = 99999999
for i in range(n):
    dist = 0
    for j in range(i, n+i):
        dist += nums[j] * (j - i)

    min_dist = min(min_dist, dist)

print(min_dist)