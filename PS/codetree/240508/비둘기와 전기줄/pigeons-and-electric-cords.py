n = int(input())

pigeons = [[] for _ in range(11)]

for _ in range(n):
    index, loc = map(int, input().strip().split(" "))
    pigeons[index].append(loc)

count = 0
for p, loc in enumerate(pigeons):
    if len(loc) < 2:
        continue
    else:
        for i in range(len(loc)-1):
            if loc[i+1] != loc[i]:
                count += 1

print(count)