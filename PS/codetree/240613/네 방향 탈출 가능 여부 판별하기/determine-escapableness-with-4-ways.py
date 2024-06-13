from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

answer = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
order = 1

q = deque()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

def push(x, y):
    global order

    answer[x][y] = order
    order += 1
    visited[x][y] = True
    q.append((x, y))


def bfs():
    dxs, dys = [1, 0, 0, -1], [0, 1, -1, 0]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                push(nx, ny)

push(0, 0)
bfs()

if answer[n-1][m-1]:
    print(1)
else:
    print(0)



# vertices_num = 7
# edges_num = 6

# graph = [[0 for _ in range(vertices_num+1)] for _ in range(vertices_num+1)]
# visited = [False for _ in range(vertices_num + 1)]
# q = deque()

# def bfs():
#     while q:
#         curr_v = q.popleft()

#         for next_v in range(1, vertices_num + 1):
#             if graph[curr_v][next_v] and not visited[next_v]:
#                 print(next_v)
#                 visited[next_v] = True
#                 q.append(next_v)


# start_points = [1, 1, 1, 2, 4, 6]
# end_points = [2, 3, 4, 5, 6, 7]

# for start, end in zip(start_points, end_points):
#     graph[start][end] = 1
#     graph[end][start] = 1

# root_vertex = 1
# print(root_vertex)
# visited[root_vertex] = True
# q.append(root_vertex)
# bfs()