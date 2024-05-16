n, m = list(map(int, input().split()))
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

def in_range(x0, y0, x1, y1):
    if not (0 <= x0 <= x1 <= m and 0 <= y0 <= y1 <= n):
        return False
    for y in range(y0, y1+1 if y1+1 < n else n):
        for x in range(x0, x1+1 if x1+1 < m else m):
            if arr[y][x] <= 0:
                return False
    
    return True

max_size = 0

for y0 in range(n):
    for x0 in range(m):
        size = 0
        for y1 in range(y0, n):
            for x1 in range(x0, m):
                if not in_range(x0, y0, x1, y1):
                    continue
                size = (y1 - y0 + 1) * (x1 - x0 + 1)
                max_size = max(size, max_size)

print(max_size if max_size != 0 else -1)