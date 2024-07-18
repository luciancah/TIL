from itertools import combinations

n, m = map(int, input().split())
group_a = [input().strip() for _ in range(n)]
group_b = [input().strip() for _ in range(n)]

possible_positions = list(combinations(range(m), 3))

count = 0

for pos in possible_positions:
    set_a = set()
    set_b = set()
    
    for row in group_a:
        set_a.add((row[pos[0]], row[pos[1]], row[pos[2]]))
    
    for row in group_b:
        set_b.add((row[pos[0]], row[pos[1]], row[pos[2]]))
    
    if set_a.isdisjoint(set_b):
        count += 1

print(count)