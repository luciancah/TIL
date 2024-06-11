n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

visited_row = [False] * n
visited_col = [False] * n

selected = []

def calc_sum(nodes):
    res = 0
    for n in nodes:
        res += grid[n[0]][n[1]]
    return res

max_sum = 0

def recur(curr_row, selected):
    global max_sum
    if len(selected) == n:
        s = calc_sum(selected)
        max_sum = max(max_sum, s)
        return

    for i in range(n):
        if not visited_col[i]:
            selected.append([curr_row, i])
            visited_row[curr_row] = True
            visited_col[i] = True
            recur(curr_row + 1, selected)
            selected.pop()
            visited_row[curr_row] = False
            visited_col[i] = False

recur(0, selected)

print(max_sum)