from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = list(map(int, input().split()))

s = SortedSet([x for x in range(1, m+1)]) # 비어있는걸로 만들기
ans = 0

for e in arr:
    right = s.bisect_right(e)

    # print(right)

    if right != 0:
        s.remove(s[right-1])
        ans += 1
    else:
        break

print(ans)