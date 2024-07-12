from collections import defaultdict

n = int(input())
# arr = []
d = defaultdict(int)


for i in range(n):
    order = list(input().split())
    if order[0] == 'add':
        d[int(order[1])] = int(order[2])
    elif order[0] == 'remove':
        d[int(order[1])] = 0
    elif order[0] == 'find':
        if d[int(order[1])]:
            print(d[int(order[1])])
        else:
            print('None')