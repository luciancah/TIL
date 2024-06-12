import sys

sys.setrecursionlimit(10000)

n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

people_num = 0
people_nums = []

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y, k):
    if not in_range(x, y):
        return False
    
    if visited[x][y] or grid[x][y] <= k:
        return False
    
    return True

def dfs(x, y, k):
    global people_num
    
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        
        if can_go(new_x, new_y, k):
            visited[new_x][new_y] = True
            
            people_num += 1
            dfs(new_x, new_y, k)

ans = [-1]
k = 1
while ans[-1] != 0:
    visited = [
        [False for _ in range(m)]
        for _ in range(n)
    ]
    people_nums = []
    for i in range(n):
        for j in range(m):
            if can_go(i, j, k):
                # print(i, j, k)
                visited[i][j] = True
                people_num = 1
                
                dfs(i, j, k)
                
                people_nums.append(people_num)
    ans.append(len(people_nums))
    k += 1

print(ans.index(max(ans)), max(ans))