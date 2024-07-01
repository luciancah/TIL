'''
매 턴 -> 카드대결 vs 카드 버리기
1. 카드대결: 서로 카드 비교, 자신 카드가 상대방보다 적으면 점수만큼 얻고 번호 작은 사람 카드 버림 / 같으면 둘다
2. 버리기: 서로 버리기
카드 소진될때 합이 최종 점수

# 남우가 i번 카드까지 봤을 때 j개 버렸을때 최대 점수
남우 i번 카드 상대방 j번 카드일 때 최대 점수
'''

n = int(input())
arr1 = [0] + list(map(int, input().split()))
arr2 = [0] + list(map(int, input().split()))

dp = [[-1] * (n+1) for _ in range(n+1)]
dp[0][0] = 0

# dp[1][0] = arr2[1] if arr2[1] < arr1[1] else 0

for i in range(n):
    for j in range(n):
        if dp[i][j] == -1:
            continue

        if arr1[i+1] < arr2[j+1]:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])

        if arr1[i+1] > arr2[j+1]:
            dp[i][j+1] = max(dp[i][j+1], dp[i][j] + arr2[j+1])

        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j])

ans = 0
for i in range(n+1):
    ans = max(ans, max(dp[i]))

print(ans)