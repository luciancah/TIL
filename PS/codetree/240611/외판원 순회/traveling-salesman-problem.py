n = int(input())
weight = []
for _ in range(n):
    weight.append(list(map(int,input().split())))

visited = [False] * n
visited[0] = True

min_dist = 999999999

def recur(count, curr_pos, dist):
    global min_dist
    if count == n:
        d = weight[curr_pos][0]
        if not d == 0:
            min_dist = min(min_dist, d+dist)
            return

    for i in range(n):
        if not visited[i] and weight[curr_pos][i] != 0:
            d = weight[curr_pos][i]
            visited[i] = True
            dist += d
            recur(count+1, i, dist)
            visited[i] = False
            dist -= d

recur(1, 0, 0)

print(min_dist)