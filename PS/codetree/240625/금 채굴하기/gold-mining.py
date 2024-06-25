n, m = map(int, input().split())
mat = []
for _ in range(n):
    line = [int(x) for x in input().split()]
    mat.append(line)
res = 0

# 각 점에서 모든 금을 커버하는 영역까지 채굴 영역을 확대하며 손해를 보지 않으며 채굴할 수 있는 금의 갯수를 갱신
for row in range(n):
    for col in range(n):
        for k in range(2 * (n-1) + 1):
            num_of_gold = sum([
            mat[i][j]
            for i in range(n)
            for j in range(n)
            if abs(row - i) + abs(col - j) <= k])
            if num_of_gold * m >= k*k+(k+1)*(k+1):
                res = max(num_of_gold, res)
print(res)
# 마름모 범위 구하는 법 유심히 보기 - 절대값 이용해서 모든 범위 체크