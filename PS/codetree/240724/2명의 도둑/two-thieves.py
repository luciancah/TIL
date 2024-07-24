n, m, c = map(int, input().split())
mat = []
for _ in range(n):
    mat.append([int(x) for x in input().split()])
a = []
max_val = 0

def intersect(a, b, c, d):
    return not b < c or d < a

def possible(sx1, sy1, sx2, sy2):
    if sy1 + m - 1 >= n or sy2 + m - 1 >= n:
        return False
    if sx1 != sx2:
        return True
    if intersect(sy1, sy1 + m - 1, sy2, sy2 + m - 1):
        return False

def find_max_value(curr_idx, curr_weight, curr_val):
    global max_val

    if curr_idx == m:
        if curr_weight <= c:
            max_val = max(curr_val, max_val)
        return
    
    find_max_value(curr_idx + 1, curr_weight, curr_val)
    find_max_value(curr_idx + 1, curr_weight + a[curr_idx], curr_val + a[curr_idx] * a[curr_idx])

    

def find_max(x, y):
    global a, max_val

    a = mat[x][y:y+m]
    max_val = 0
    find_max_value(0, 0, 0)
    return max_val

ans = max([
        find_max(sx1, sy1) + find_max(sx2, sy2)
        for sx1 in range(n)
        for sy1 in range(n)
        for sx2 in range(n)
        for sy2 in range(n)
        if possible(sx1, sy1, sx2, sy2)
    ])
print(ans)