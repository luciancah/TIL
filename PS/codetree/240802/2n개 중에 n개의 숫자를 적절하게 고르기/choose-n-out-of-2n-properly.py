n = int(input())
buf = [int(x) for x in input().split()]
group = []
ans = sum(buf)

def try_combinations(curr_idx):
    global ans, group, buf
    if len(group) == n:
        # print(buf, group)
        ans = min(ans, abs(sum(buf) - 2 * sum(group)))
        return
    for i in range(curr_idx, len(buf)):
        group.append(buf[i])
        try_combinations(i + 1)
        group.pop()

try_combinations(0)
print(ans)