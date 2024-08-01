import sys
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

'''
거리 미니멈 k로 할 수 있는지 이분탐색 (min 1 max max(arr))
'''

left = 1
right = sys.maxsize
ans = 1

def get_ans(num):
    count = 0
    offset = 0

    for i in range(1, len(arr)):
        offset += arr[i] - arr[i-1]
        if offset >= num:
            count += 1
            offset = 0

    return count



while left <= right:
    mid = (left + right) // 2
    
    if get_ans(mid)+1 >= m:
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1


print(ans)