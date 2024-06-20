n = int(input())
lines = []
for _ in range(n):
    lines.append(list(map(int, input().split())))


'''
원래 접근 : combination 만들어서 걔네 겹치는지 확인 - 최댓값 구하기 (완탐)
nC(1~n) 하면 터지긴 할듯

선분 하나마다 고르고 말고 선택하기 dp배열은 멀로 ? ...
'''

def is_crossed(l1, l2):
    # l1 and l2 are tuples or lists representing the line segments as (start, end)
    # Ensure l1 is ordered such that l1[0] <= l1[1]
    if l1[0] > l1[1]:
        l1 = (l1[1], l1[0])
    # Ensure l2 is ordered such that l2[0] <= l2[1]
    if l2[0] > l2[1]:
        l2 = (l2[1], l2[0])
    
    # Check if the segments overlap
    return not (l1[1] < l2[0] or l2[1] < l1[0])

ans = 0

lines.sort(key=lambda x: x[0])

dp = [1] * n
# dp[k] = 1
for i in range(n):
    max_dp = 1
    for j in range(0, i):
        if not is_crossed(lines[i], lines[j]):
            max_dp = max(max_dp, dp[j] + 1)

    dp[i] = max_dp

ans = max(max(dp), ans)
# print(dp)

print(ans)