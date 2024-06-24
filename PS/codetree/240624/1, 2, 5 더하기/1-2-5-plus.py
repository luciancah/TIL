'''
dp배열 -> 구하는게 경우의 수 니까 -> 숫자 i를 만들기 위한 경우의 수 저장 -> 더하기
'''

n = int(input())
nums = [1, 2, 5]
dp = [0 for _ in range(n+1)]

dp[0] = 1

for i in range(1, n+1):
    for j in range(3):
        if i >= nums[j]:
            dp[i] = (dp[i] + dp[i-nums[j]]) % 10007

print(dp[-1])