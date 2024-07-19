n, m = map(int, input().split())
lines = []
for _ in range(m):
    a, b = tuple(map(int, input().split()))
    lines.append((b, a - 1))
lines.sort()
selected_lines = []
ans = m

def run_ladder():
    num1, num2 = [i for i in range(n)], [i for i in range(n)]

    # 이걸 얶떢께 생각함? ㅋㅋ 천잰가
    for _, idx in lines:
        num1[idx], num1[idx + 1] = num1[idx + 1], num1[idx]
    for _, idx in selected_lines:
        num2[idx], num2[idx + 1] = num2[idx + 1], num2[idx]

    for i in range(n):
        if num1[i] != num2[i]:
            return False
    return True

def find_min_lines(cnt):
    global ans

    if cnt == m:
        if run_ladder():
            ans = min(ans, len(selected_lines))
        return
    
    selected_lines.append(lines[cnt])
    find_min_lines(cnt + 1)
    selected_lines.pop()

    find_min_lines(cnt + 1)

find_min_lines(0)
print(ans)