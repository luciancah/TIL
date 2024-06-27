n = int(input())
mat = []
for _ in range(n):
    mat.append([int(x) for x in input().split()])

max_sum = 0

def get_max_sum_in_range(row, col, k):
    if row < k - 1 or col < k - 1: return 0
    dxs, dys = [1, -1, -1, 1], [-1, -1, 1, 1]
    dx, dy = dxs[0], dys[0]
    x = col - k + 2
    y = row
    # print(y, x, k)
    k_range_max = 0
    for x in range(col - k + 2, col):
        # print(x)
        range_max = 0
        i = 0
        dx, dy = dxs[0], dys[0]
        x_offset = x
        y_offset = y
        while True:
            if col-k+1 <= x_offset <= col and row-k+1 <= y_offset <= row:
                # if k == 5:
                #     print(y_offset, x_offset)
                range_max += mat[y_offset][x_offset]
            else:
                x_offset -= dx
                y_offset -= dy
                i += 1
                dx, dy = dxs[i], dys[i]
            x_offset += dx
            y_offset += dy
            if x_offset == x and y_offset == y: break
        # print(range_max)
        k_range_max = max(range_max, k_range_max)
    return k_range_max

for row in range(n):
    for col in range(n):
        if n == 3:
            max_sum = max(get_max_sum_in_range(row, col, 3), max_sum)
        for k in range(3, n+1):
            max_sum = max(get_max_sum_in_range(row, col, k), max_sum)

print(max_sum)