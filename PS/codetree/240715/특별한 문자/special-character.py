from collections import defaultdict

string = list(input())

d = defaultdict(int)

for s in string:
    d[s] += 1

d2 = sorted(list(d.items()), key=lambda x:x[1])

print(d2[0][0]) if d2[0][1] == 1 else print('None')