n = int(input())

left = 1
right = n
max_num = 1

while left <= right:
    mid = (left + right) // 2
    if mid * (mid + 1) // 2 > n:
        right = mid - 1
    else:
        left = mid + 1
        max_num = max(max_num, mid)

print(max_num)