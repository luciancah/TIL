from sortedcontainers import SortedDict

n = int(input())
words = [input() for _ in range(n)]

sd = SortedDict()

for w in words:
    if w in sd:
        sd[w] += 1
    else:
        sd[w] = 1

sd = list(sd.items())

for s in sd:
    print(" ".join(map(str, s)))