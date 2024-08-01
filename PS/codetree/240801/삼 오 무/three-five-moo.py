import sys

n = int(input())

def get_count(num):
    ans = num
    ans -= num // 3
    ans -= num // 5
    ans += num // 15

    return ans

left = 1
right = sys.maxsize
ans = sys.maxsize

while left <= right:
    mid = (left + right) // 2
    count = get_count(mid)

    if count < n:
        left = mid + 1
    else:
        ans = min(mid, ans)
        right = mid - 1

print(ans)