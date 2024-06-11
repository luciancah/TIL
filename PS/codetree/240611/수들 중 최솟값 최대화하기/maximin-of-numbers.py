n = int(input())
grid = []

for _ in range(n):
    grid.append(list(map(int, input().split())))

visited_row = [False] * n
visited_col = [False] * n

selected = []

max_selected = 0

def calc_min_selected(arr):
    m = 99999
    for i in range(len(arr)):
        m = min(m, grid[arr[i][0]][arr[i][1]])

    return m


def recur(curr_row, selected):
    global max_selected
    if len(selected) == n:
        local_min_selected = calc_min_selected(selected)
        max_selected = max(local_min_selected, max_selected)
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

print(max_selected)