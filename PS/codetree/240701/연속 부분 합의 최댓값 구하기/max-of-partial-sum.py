'''
dp배열 : dp[i] 위치에서 끝나는 연속 수열이 얻을 수 있는 최대 점수

1. 그 이전 연속 부분 수열에 i번째 원소 추가하는 경우
2. i 위치에서 연속 부분 수열 시작하는 경우
'''

import sys
int_min = -sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

dp = [int_min] * (n)
dp[0] = arr[0]

for i in range(1, n):
    if dp[i-1] == int_min:
        continue
    dp[i] = max(arr[i], dp[i-1] + arr[i])

print(max(dp))