'''
2n개 주어졌을 때 순서 유지 n개 골라서 홀수번째 더하고 짝수번째 빼기
i위치에서 j개 골랐을 때 값 (2차원)

- i 위치 고르지 않는 경우 == i-1 위치에서 j개 골랐을 때
- i 위치 고르는 경우 == i-1 위치에서 j-1개 == i위치에서 j개

n층 높이일 때 1계단 / 2계단 올라가기 (1계단은 최대 3회)
i층일 때 1계단 j회 올라 갔을 때 값 동전의 총액
'''

import sys
int_min = -sys.maxsize

n = int(input())
arr = [0] + list(map(int, input().split()))

dp = [[int_min]  * (4) for _ in range(n+1)]

dp[0][0] = 0
dp[1][0] = int_min
dp[1][1] = arr[1]
dp[2][0] = arr[2]

for i in range(2, n+1):
    for j in range(4):
        # if i == 4 and j == 0:
        #     print(dp[i-1][j-1] + arr[i], dp[i-2][j] + arr[i], dp[i-1][j-1], arr[i])
        if j-1 >= 0 and i-1 >= 0 and dp[i-1][j-1] != int_min:
            dp[i][j] = dp[i-1][j-1] + arr[i]
        if i-2 >= 0 and j >=0 and dp[i-2][j] != int_min:
            dp[i][j] = max(dp[i][j], dp[i-2][j] + arr[i])

# print(dp)
print(max(dp[-1]))
# 0 [0, x, x, x]
# 1 [0, 1, x, x]
# 2 [2, 2, 3, x]
# 3 [3, 5, 5, 6]
# 4 [10, 7, 9, 9]

# 0 [0, x, x, x]
# 3 [x, 3, x, x]
# 7 [7, x, 10, x]
# 11 [x, 18, x, 21]
# 2 [9, x, 20, x]
# 9 [x, 27, x, 30]
# 6 [15, x, 33, x]