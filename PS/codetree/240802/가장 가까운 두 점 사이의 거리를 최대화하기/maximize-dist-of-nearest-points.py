import sys

n = int(input())
segments = [list(map(int, input().split())) for _ in range(n)]
segments.sort()

def is_possible(dist):
        # 첫번째 선분의 시작점을 선택
        cnt = 1
        curr_x = segments[0][0]

        for i in range(1, n):
            a, b = segments[i]
            if curr_x + dist <= b:
                cnt += 1
                curr_x = max(a, curr_x + dist)
            else:
                # 다음 가능한 위치로 이동
                curr_x = max(curr_x, a)

            if cnt >= n:
                return True

        return cnt >= n

left = 1
right = sys.maxsize
ans = 0

while left <= right:
    mid = (left + right) // 2
    
    if is_possible(mid):
        left = mid + 1
        ans = max(ans, mid)
    else:
        right = mid - 1

print(ans)