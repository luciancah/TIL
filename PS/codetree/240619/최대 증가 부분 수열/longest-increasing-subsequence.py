import sys

n = int(input())
dp = [0] * n
a = list(map(int, input().split()))

# 점화식 : 배열 순회하면서 현재 원소 위치에서 가장 긴 증가 부분 수열 길이 구하기


def init():
    for i in range(n):
        dp[i] = -sys.maxsize

    dp[0] = 1

init()

for i in range(1, n):
    for j in range(0, i):
        if a[j] < a[i]:
            if dp[j] == -sys.maxsize:
                dp[j] = 1
            # print(j, i)
            dp[i] = max(dp[j] + 1, dp[i])


# print(dp)

ans = 0
for i in range(n):
    ans = max(ans, dp[i])

print(ans)