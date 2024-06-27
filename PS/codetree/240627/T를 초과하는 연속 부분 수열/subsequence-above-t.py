n, t = map(int, input().split())
nums = list(map(int, input().split()))
max_count = 0
for i in range(n):
    count = 0
    for j in range(i, n):
        if nums[j] > t:
            count += 1
        else:
            break
    max_count = max(max_count, count)

print(max_count)