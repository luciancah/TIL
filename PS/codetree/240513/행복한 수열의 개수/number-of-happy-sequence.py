n, m = list(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr2 = [list(x) for x in zip(*arr)]

fullcount = 0
count = 0

if m == 1:
    print(2*n)

else:
    # 가로순회
    for a1 in arr:
        for i in range(1, len(a1)):
            if a1[i-1] == a1[i]:
                count += 1
                if count >= m-1:
                    count = 0
                    fullcount += 1
                    break
            else:
                count = 0

    # 가로순회
    for a2 in arr2:
        for i in range(1, len(a2)):
            if a2[i-1] == a2[i]:
                count += 1
                if count >= m-1:
                    count = 0
                    fullcount += 1
                    break
            else:
                count = 0

    print(fullcount)