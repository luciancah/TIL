import sys

n, m = map(int, input().split())
arr = [int(input()) for _ in range(m)]

def get_count(num):
    count = 0
    for a in arr:
        count += num // a

    return count

left = 1
right = sys.maxsize
ans = right

while left <= right:
    mid = (left + right) // 2
    
    if get_count(mid) >= n:
        ans = min(ans, mid)
        right = mid - 1
    else:
        left = mid + 1

print(ans)