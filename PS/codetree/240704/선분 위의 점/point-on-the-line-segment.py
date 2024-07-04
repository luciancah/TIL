n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
lines = [sorted(list(map(int, input().split()))) for _ in range(m)]


def lower_bound(arr, target):
    left, right = 0, n-1
    min_index = n

    while left <= right:
        mid = (left + right) // 2
        if target <= arr[mid]:
            min_index = min(min_index, mid)
            right = mid - 1
        else:
            left = mid + 1

    return min_index

def upper_bound(arr, target):
    left, right = 0, n-1
    min_index = n

    while left <= right:
        mid = (left + right) // 2
        if target < arr[mid]:
            min_index = min(min_index, mid)
            right = mid - 1
        else:
            left = mid + 1

    return min_index

for u in lines:
    lb, ub = lower_bound(arr, u[0]), upper_bound(arr, u[1])
    print(ub - lb)