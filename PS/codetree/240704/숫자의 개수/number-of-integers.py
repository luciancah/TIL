n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = [int(input()) for _ in range(m)]

def lower_bound(arr, target):
    left = 0
    right = n-1
    min_index = n

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            min_index = min(min_index, mid)
            right = mid - 1
        else:
            left = mid + 1

    return min_index

def upper_bound(arr, target):
    left = 0
    right = n-1
    min_index = n

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            min_index = min(min_index, mid)
            right = mid - 1
        else:
            left = mid + 1
    
    return min_index

def custom_bound(arr, target):
    left = 0
    right = n-1
    max_index = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            max_index = max(max_index, mid)
            left = mid + 1
        else:
            right = mid - 1

    return max_index

for u in nums:
    lb, ub = lower_bound(arr, u), upper_bound(arr, u)
    print(ub - lb)