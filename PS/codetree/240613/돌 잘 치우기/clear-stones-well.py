from collections import deque
from itertools import combinations

n, k, m = map(int, input().split())
grid2 = [list(map(int, input().split())) for _ in range(n)]
empty = [[0] * n for _ in range(n)]
# grid = grid2[:]
starts = [list(map(int, input().split())) for _ in range(k)]
starts = [[r-1, c-1] for r, c in starts]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y]:
        return False
    return True

def push(x, y):
    q.append((x, y))
    visited[x][y] = 1

def calc_visited(grid):
    res = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                res += 1

    return res

dxs, dys = [1, 0, 0, -1], [0, 1, -1, 0]

def bfs():
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                push(nx, ny)

rocks = []
for i in range(n):
    for j in range(n):
        if grid2[i][j] == 1:
            rocks.append([i, j])

# print(rocks)

def create_grid(r, grid):
    for i in range(n):
        for j in range(n):
            if [i, j] in r:
                grid[i][j] = 1
    return grid

max_visited = 0

for nr in combinations(rocks, len(rocks)-m):
#   print(nr, rocks, len(rocks)-m)
  empty = [[0] * n for _ in range(n)]
  grid = create_grid(list(nr), empty)

#   for i in range(n):
#       print(*grid[i])
#   print()


  visited = [[0] * n for _ in range(n)]
  

  for r, c in starts:
      q = deque()
      push(r, c)
      bfs()
    #   print('-------')
    #   print(calc_visited(visited))
      max_visited = max(calc_visited(visited), max_visited)

print(max_visited)