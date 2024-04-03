n = int(input())
ㅁㄱㄱ = []

for i in range(n):
    ㅁㄱㄱ.append([int(x) for x in input().split()] + [i+1])

ㅁㄱㄱ.sort(key=lambda x : [x[0], -x[1]])


for i in ㅁㄱㄱ:
    print(*i)