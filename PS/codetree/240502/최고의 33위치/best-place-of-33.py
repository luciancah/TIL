n = int(input())
m = []
for _ in range(n):
    m.append([int(x) for x in input().split()])
max_coin = 0
for i in range(n - 2):
    for k in range(n - 2):
        total = 0
        for c in range(3):
            for d in range(3):
                if m[i + c][k + d] == 1:
                    total += 1
        if total > max_coin:
            max_coin = total
print(max_coin)