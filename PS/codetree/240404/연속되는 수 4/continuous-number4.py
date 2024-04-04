n = int(input())
numbers = [int(input()) for _ in range(n)]

ans, count = 0, 0
for i in range(n):
    if i >= 1 and numbers[i] > numbers[i-1]:
        count += 1
    else:
        count = 1

    ans = max(ans, count)

print(ans)