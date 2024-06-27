def search_section(x, y, dest_x, dest_y):
    # print(x, y, dest_x, dest_y)
    for i in range(y, dest_y + 1):
        for j in range(x, dest_x + 1):
            if mat[i][j] <= 0:
                # print('no')
                return 0
    # print((dest_x - x + 1) * (dest_y - y + 1))
    return abs(dest_x - x + 1) * abs(dest_y - y + 1)

def get_max_rec(row, col):
    range_max = 0
    x_offset, y_offset = col, row
    for y_offset in range(row, n):
        for x_offset in range(col, m):
            range_max = max(range_max, search_section(col, row, x_offset, y_offset))
    return range_max

n, m = map(int, input().split())
mat = []
for _ in range(n):
    mat.append([int(x) for x in input().split()])
max_size = 0
for row in range(n):
    for col in range(m):
        max_size = max(max_size, get_max_rec(row, col))
if max_size == 0:
    print(-1)
else:
    print(max_size)