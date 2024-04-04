n, t = list(map(int, input().split()))
numbers = list(map(int, input().split()))

ans, count = 0, 0
for i in range(n):
    if numbers[i] > t:
        count += 1
    else:
        count = 0

    ans = max(ans, count)

print(ans)