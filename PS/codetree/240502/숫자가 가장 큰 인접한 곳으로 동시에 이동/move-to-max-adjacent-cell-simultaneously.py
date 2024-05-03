def print_arr(arr):
    for i in arr:
        print(i)

n, m, t = map(int, input().split())
matrix = []
count = [[0 for col in range(n)] for row in range(n)]
n_count = [[0 for col in range(n)] for row in range(n)]
for _ in range(n):
    matrix.append([int(x) for x in input().split()])
for _ in range(m):
    r, c = map(int, input().split())
    count[r - 1][c - 1] = 1

# print_arr(matrix)
dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]
for s in range(t):
    for i in range(n):
        for k in range(n):
            if count[i][k]:
                x, y = k, i
                max_val = -1
                mx, my = x, y
                for j in range(4):
                    nx, ny = x + dxs[j], y + dys[j]
                    if nx > n - 1 or nx < 0 or ny > n - 1 or ny < 0:
                        continue
                    if matrix[ny][nx] > max_val:
                        max_val = matrix[ny][nx]
                        mx = nx
                        my = ny
                n_count[my][mx] += 1
    # print('-----------------')
    # print(s, 'count')
    # print_arr(count)
    # print('n_count')
    # print_arr(n_count)
    # print('-----------------')
    for item in n_count:
        for idx in range(len(item)):
            if item[idx] >= 2:
                item[idx] = 0
    # print_arr(n_count)
    count = n_count
    n_count = [[0 for col in range(n)] for row in range(n)]
total = 0
for item in count:
    for idx in range(len(item)):
        if item[idx]:
            total += 1
print(total)