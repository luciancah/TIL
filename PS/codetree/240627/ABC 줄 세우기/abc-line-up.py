n = int(input())
ppls = list(map(str, input().split()))

# 스왑해서 소트하는거 구현하기 + 횟수 세기
count = 0
for i in range(n-1):
    for j in range(i, n):
        if ppls[i] > ppls[j]:
            # print(ppls[i], ppls[j])
            count += 1
            ppls[i], ppls[j] = ppls[j], ppls[i]

    # print(ppls)
print(count)