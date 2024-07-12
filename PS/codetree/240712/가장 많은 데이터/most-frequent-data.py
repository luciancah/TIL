from collections import defaultdict

n = int(input())
words = [input() for _ in range(n)]

d = defaultdict(int)

for i, e in enumerate(words):
    d[e] += 1

d = sorted(d.items(), key=lambda x:-x[1])
print(d[0][1])