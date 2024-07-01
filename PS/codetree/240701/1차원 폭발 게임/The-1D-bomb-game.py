n, m = map(int, input().split())
q = []
for _ in range(n):
    q.append(int(input()))

while True:
    i = 0
    buf = []
    while i < len(q):
        buf.append(q[i])
        prev = q[i]
        start = i
        i += 1
        while i < len(q) and q[i] == prev:
            buf.append(q[i])
            i += 1
        if i - start >= m:
            for k in range(start, i):
                q[k] = 'x'
                buf.pop()
    if buf == q: break
    q = buf
print(len(q))
for b in q:
    print(b)