n, m = list(map(int, input().split()))
ans = []

def recur(ans, count):
    if count == m:
        print(*ans)
        return
    
    for i in range(ans[-1], n+1):
        if i not in ans:
            ans.append(i)
            recur(ans, count + 1)
            ans.pop()

for i in range(1, n+1):
    ans.append(i)
    recur(ans, 1)
    ans.pop()