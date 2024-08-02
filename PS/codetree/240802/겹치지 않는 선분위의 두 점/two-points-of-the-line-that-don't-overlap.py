import sys

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

# 가장 가까운 두 점의 거리 최댓값 x로 두고 점 n개 찍을 수 있는지

left = 1
right = sys.maxsize
ans = 0


arr.sort()

def can_place(num):
    count = 1
    last_point = arr[0][0]

    i = 0
    while i < m:
        if last_point + num <= arr[i][1]:
            if arr[i][0] <= last_point + num:
                count += 1
                last_point = last_point + num
            else:
                count += 1
                last_point = arr[i][0]
        else:
            i += 1

    return count

while left <= right:
    mid = (left + right) // 2

    if can_place(mid) >= n:
        left = mid + 1
        ans = max(ans, mid)
    else:
        right = mid - 1

print(ans)