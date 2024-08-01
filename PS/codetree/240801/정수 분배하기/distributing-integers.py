import sys
INT_MAX = sys.maxsize

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# 정수 K를 목표로 두고 m개 이상 만들 수 있는 최대의 k 파라메트릭 하기

left = 1
right = max(arr)
ans = 0

def is_possible(max_sum):
    total = 0

    for a in arr:
        total += a // max_sum
    
    if total >= m:
        return True
    else:
        return False

while left <= right:
    mid = (left + right) // 2

    if is_possible(mid):
        left = mid + 1
        ans = max(ans, mid)
    else:
        right = mid - 1

print(ans)