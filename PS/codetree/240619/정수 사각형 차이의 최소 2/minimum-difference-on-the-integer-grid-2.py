import sys

INT_MAX = sys.maxsize
MAX_R = 100

# 변수 선언 및 입력:
n = int(input())
num = [
    list(map(int, input().split()))
    for _ in range(n)
]
dp = [
    [
        [INT_MAX] * (MAX_R + 1)
        for _ in range(n)
    ]
    for _ in range(n)
]

def initialize():
    # 전부 INT_MAX로 초기화합니다.
    for i in range(n):
        for j in range(n):
            for k in range(1, MAX_R + 1):
                dp[i][j][k] = INT_MAX

    # 시작점의 경우 dp[0][0][num[0][0]] = num[0][0]으로 초기값을 설정해줍니다
    dp[0][0][num[0][0]] = num[0][0]

    # 최좌측 열의 초기값을 설정해줍니다.
    for i in range(1, n):
        for k in range(1, MAX_R + 1):
            dp[i][0][min(k, num[i][0])] = min(
                dp[i][0][min(k, num[i][0])],
                max(dp[i - 1][0][k], num[i][0])
            )

    # 최상단 행의 초기값을 설정해줍니다.
    for j in range(1, n):
        for k in range(1, MAX_R + 1):
            dp[0][j][min(k, num[0][j])] = min(
                dp[0][j][min(k, num[0][j])],
                max(dp[0][j - 1][k], num[0][j])
            )

def solve():
    # DP 초기값 설정
    initialize()

    # 탐색하는 위치의 위에 값과 좌측 값 중에 작은 값과
    # 해당 위치의 숫자 중에 최댓값을 구해줍니다.
    for i in range(1, n):
        for j in range(1, n):
            for k in range(1, MAX_R + 1):
                dp[i][j][min(k, num[i][j])] = min(
                    dp[i][j][min(k, num[i][j])],
                    max(min(dp[i - 1][j][k], dp[i][j - 1][k]), num[i][j])
                )

   
# DP로 문제를 해결합니다.
solve()

# 가능한 답 중 최적의 답을 계산합니다.
ans = INT_MAX
for k in range(1, MAX_R + 1):
    if dp[n - 1][n - 1][k] != INT_MAX:
        ans = min(ans, dp[n - 1][n - 1][k] - k)

print(ans)