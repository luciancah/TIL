vertices_num, edges_num = map(int, input().split())
edges = []

for _ in range(edges_num):
    edges.append(list(map(int, input().split())))

graph = [
    [0 for _ in range(vertices_num + 1)]
    for _ in range(vertices_num + 1)
]
visited = [False for _ in range(vertices_num + 1)]

for start, end in edges:
    graph[start][end] = 1
    graph[end][start] = 1

def dfs(vertex):
    global count

    for curr_v in range(1, vertices_num + 1):
        if graph[vertex][curr_v] and not visited[curr_v]:
            count += 1
            visited[curr_v] = True
            dfs(curr_v)

count = 0
root_vertex = 1
# print(root_vertex)
visited[root_vertex] = True
dfs(root_vertex)
print(count)

'''
adjacent list

graph = [
    [[] for _ in range(VERTICES_NUM + 1)]
]
visited = [False for _ in range(VERTICES_NUM + 1)]

start_points = [1, 1, 1, 2, 4, 6]
end_points = [2, 3, 4, 5, 6, 7]

for start, end in zip(start_points, end_points):
    graph[start].append(end)
    graph[end].append(start)

def dfs2(vertex):
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            print(curr_v)
            visited[curr_v] = True
            dfs(curr_v)
'''