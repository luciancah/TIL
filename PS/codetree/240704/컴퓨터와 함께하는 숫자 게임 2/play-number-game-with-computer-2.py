import sys

m = int(input())
a, b = map(int, input().split())

def bisect(target):
    left, right = 1, m
    # index = -1
    count = 0

    while left <= right:
        mid = (left + right) // 2
        count += 1

        if mid == target:
            # index = mid
            break
        if mid > target:
            right = mid - 1
        else:
            left = mid + 1

    return count

# arr = [x for x in range(1, m+1)]
min_ans = sys.maxsize
max_ans = -sys.maxsize

for i in range(a, b+1):
    c = bisect(i)
    min_ans = min(min_ans, c)
    max_ans = max(max_ans, c)

print(min_ans, max_ans)