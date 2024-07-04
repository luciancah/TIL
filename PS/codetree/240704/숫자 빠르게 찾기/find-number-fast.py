n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = [int(input()) for _ in range(m)]


def bisect(arr, target):
    index = -2
    left, right = 0, n-1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            index = mid
            break
        
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return index

# print(bisect(arr, 99))
for u in nums:
    print(bisect(arr, u) + 1)