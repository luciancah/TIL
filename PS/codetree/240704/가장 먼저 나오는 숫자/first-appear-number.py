n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

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

def lower_bound(arr, target):
    left, right = 0, n-1
    min_index = n-1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            min_index = min(min_index, mid)
            right = mid - 1
        else:
            left = mid + 1

    return min_index

for u in nums:
    res = lower_bound(arr, u)
    if arr[res] == u:
        print(res + 1)
    else:
        print('-1')