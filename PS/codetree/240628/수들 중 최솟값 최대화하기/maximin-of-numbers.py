import sys

sys.setrecursionlimit(600000)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [0 for _ in range(n)]

ans = 0
selected = []

def recur(row):
    global ans

    if len(selected) == n:
        ans = max(ans, min(selected))
        return
        
    
    for i in range(n):
        if not visited[i]:
            selected.append(grid[row][i])
            visited[i] = 1
            recur(row + 1)
            selected.pop()
            visited[i] = 0

    return

recur(0)
print(ans)