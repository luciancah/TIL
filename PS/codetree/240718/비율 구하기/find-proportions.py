from sortedcontainers import SortedDict

n = int(input())
sd = SortedDict()

for _ in range(n):
    string = input()
    if string in sd:
        sd[string] += 1
    else:
        sd[string] = 1

for k, v in list(sd.items()):
    print(f'{k} {round(v*100/n, 4):.4f}')