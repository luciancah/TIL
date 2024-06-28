import sys

sys.setrecursionlimit(10000)

n, m = map(int, input().split())
dots = [list(map(int, input().split())) for _ in range(n)]

def calc_dist(d1, d2):
    return (d1[0]-d2[0]) ** 2 + (d1[1]-d2[1]) ** 2

ans = sys.maxsize

def recur(count, idx, selected):
    global ans
    dist = 0
    if len(selected) == m:
        # print(selected)
        for i in range(m):
            for j in range(i+1, m):
                dist = max(dist, calc_dist(selected[i], selected[j]))
        ans = min(ans, dist)
        return
    if idx == n:
        return
    
    selected.append(dots[idx])
    recur(count+1, idx+1, selected)
    selected.pop()
    recur(count, idx+1, selected)

    return

recur(0, 0, [])
print(ans)