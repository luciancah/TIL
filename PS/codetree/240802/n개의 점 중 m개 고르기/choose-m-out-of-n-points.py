import math 

n, m = map(int, input().split())
dots = []
selected = []
ans = math.inf
for _ in range(n):
    dots.append([int(x) for x in input().split()])

def get_max_dist():
    global selected
    max_dist = 0
    for i in range(m):
        for j in range(i + 1, m):
            dist = pow(selected[i][0] - selected[j][0], 2) + pow(selected[i][1] - selected[j][1], 2)
            max_dist = max(max_dist, dist)
    return max_dist

def get_combination(curr_idx):
    global dots, selected, ans
    if len(selected) >= m:
        ans = min(ans, get_max_dist())
        return
    for i in range(curr_idx, len(dots)):
        selected.append(dots[i])
        get_combination(i + 1)
        selected.pop()

get_combination(0)
print(ans)