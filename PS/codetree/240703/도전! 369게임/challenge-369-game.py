MOD = 10**9 + 7

a = input()
n = len(a)

pt = [1] * (n + 1)
for i in range(1, n + 1):
    pt[i] = pt[i - 1] * 10 % MOD

# dp[i][j] :: 앞 i번째 자릿수까지 봤을 때, 각 자릿수의 합이 3의 배수이며, 자릿수 중 3, 6, 9가 나타나지 않았으며,
# 이 뒤에 0 ~ 9 중 어느 숫자를 붙여도 되는 형태의 자릿수의 개수
dp = [[0 for _ in range(3)] for _ in range(100001)]
ans = 0
is_suc = False
sm = 0

for i in range(n):
    num = int(a[i])
    for x in range(10):
        # 3, 6, 9인 경우 별도로 처리합니다.
        if x in [3, 6, 9]:
            ans += (dp[i][0] + dp[i][1] + dp[i][2]) * pt[n - i - 1] % MOD
            ans %= MOD
            continue
        
        # 나머지 숫자들에 대한 dp 계산을 수행합니다.
        for k in range(3):
            dp[i + 1][(x + k) % 3] += dp[i][k]
            dp[i + 1][(x + k) % 3] %= MOD

    # 현재 숫자가 num보다 작은 경우를 처리합니다.
    for x in range(num):
        if is_suc or x in [3, 6, 9]:
            ans += pt[n - i - 1]
            ans %= MOD
        else:
            dp[i + 1][(x + sm) % 3] += 1
            dp[i + 1][(x + sm) % 3] %= MOD

    # 현재 숫자가 3, 6, 9인 경우 플래그를 설정합니다.
    if num in [3, 6, 9]:
        is_suc = True
    else:
        sm += num

# 마지막 자릿수를 처리합니다.
if is_suc:
    ans += 1
    ans %= MOD
else:
    dp[n][sm % 3] += 1
    dp[n][sm % 3] %= MOD

# 최종 결과를 계산하여 출력합니다.
ans += dp[n][0]
ans += (MOD - 1);
ans %= MOD
print(ans)