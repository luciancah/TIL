import sys
max_ans = sys.maxsize

n, m = map(int, input().split())
quests = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
sum_value = 0
for i in range(len(quests)):
    sum_value += quests[i][0]

dp = [max_ans for _ in range(sum_value + 1)]
dp[0] = 0

for i in range(1, n+1):
    for j in range(sum_value, -1, -1):
        if j >= quests[i][0]:
            if dp[j-quests[i][0]] == max_ans:
                continue
            dp[j] = min(dp[j], dp[j-quests[i][0]] + quests[i][1])

# print(m, sum_value)
# print(dp[m:])
if len(dp[m:]):
    print(min(dp[m:]))
else:
    print(-1)