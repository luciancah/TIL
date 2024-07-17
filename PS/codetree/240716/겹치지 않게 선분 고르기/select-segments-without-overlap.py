n = int(input())
lines = []
for _ in range(n):
    lines.append([int(x) for x in input().split()])
max_l = 0

def backtrack(compatibles, remainings):
    global max_l
    done = 1
    for i in range(len(remainings)):
        l = remainings[i]
        available = 1
        for c in compatibles:
            if l[0] >= c[0] and l[0] <= c[1] or l[1] >= c[0] and l[1] <= c[1] or l[0] <= c[0] and l[1] >= c[1]:
                available = 0
                break
        if available:
            done = 0
            buf_c = [arr[:] for arr in compatibles]
            buf_r = [arr[:] for arr in remainings]
            buf_c.append(l)
            buf_r.pop(i)
            backtrack(buf_c, buf_r)
            return
    if done:
        max_l = max(max_l, len(compatibles))

for i in range(len(lines)):
    buf = [arr[:] for arr in lines]
    targ = buf.pop(i)
    backtrack([targ], buf)
print(max_l)