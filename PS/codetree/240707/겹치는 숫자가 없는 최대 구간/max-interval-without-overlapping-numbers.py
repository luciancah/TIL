from collections import defaultdict

n = int(input())
arr = list(map(int, input().split()))

j = 0
ans = 0
cache = defaultdict(bool)
count = 0
for i in range(n):
    while j < n and not cache[arr[j]]:
        cache[arr[j]] = True
        count += 1
        j += 1
    ans = max(ans, count)
    # print(count, cache)
    count -= 1
    cache[arr[i]] = False

print(ans)