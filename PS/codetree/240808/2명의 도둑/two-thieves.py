n, m, c = map(int, input().split())
mat = []
for _ in range(n):
    mat.append([int(x) for x in input().split()])
a = []
max_val = 0

# 겹치면 False다.
def intersect(a, b, c, d):
    return not (b < c or d < a)

# 문제의 조건에 부합하는지 체크한다.
def possible(sx1, sy1, sx2, sy2):
    if sy1 + m - 1 >= n or sy2 + m - 1 >= n:
        return False
    if sx1 != sx2:
        return True
    if intersect(sy1, sy1 + m - 1, sy2, sy2 + m - 1):
        return False
    return True

# 백트레킹 함수. 각 지점을 포함할 수도, 안할수도 있다.
def backtrack(curr_idx, curr_weight, curr_val):
    global max_val
    if curr_idx >= m:
        if curr_weight <= c:
            max_val = max(max_val, curr_val)
        return
    
    backtrack(curr_idx + 1, curr_weight, curr_val)
    backtrack(curr_idx + 1, curr_weight + a[curr_idx],
    curr_val + a[curr_idx] * a[curr_idx])

# (row, col)좌표에서 m만큼 배열을 잘라내서 백트레킹한다.
def get_max(col, row):
    global max_val, a

    a = mat[row][col:col+m]
    max_val = 0
    backtrack(0, 0, 0)
    return max_val

ans = max([
    get_max(col1, row1) + get_max(col2, row2)
    for col1 in range(n)
    for row1 in range(n)
    for col2 in range(n)
    for row2 in range(n)
    if possible(row1, col1, row2, col2)
])

print(ans)