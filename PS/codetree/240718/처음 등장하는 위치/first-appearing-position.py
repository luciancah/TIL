from sortedcontainers import SortedDict

n = int(input())
arr = list(map(int, input().split()))

sd = SortedDict()

for i, e in enumerate(arr):
    if e not in sd:
        sd[e] = i+1

res = list(sd.items())
for i in range(len(res)):
    print(" ".join(map(str, res[i])))