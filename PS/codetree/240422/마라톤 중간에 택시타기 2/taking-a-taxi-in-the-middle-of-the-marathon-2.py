n = int(input())
checks = []
for _ in range(n):
    checks.append(list(map(int, input().split())))

dists = []
'''
완탐 하는데
1개씩 뺀 거리 다 더한거 구해서 거기서 min 잡기
'''

for i in range(n):
    dist = checks[:]
    if i > 0 and i < n-1:
        dist.remove(checks[i])
        dists.append(dist)
    
min_dist = 9999999
for i in range(len(dists)):
    dist = 0
    for j in range(1, len(dists[i])):
        dist += abs(dists[i][j-1][0] - dists[i][j][0]) + abs(dists[i][j][1] - dists[i][j-1][1])

    min_dist = min(dist, min_dist)
    

print(min_dist)