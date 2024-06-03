n, m = list(map(int, input().split()))
lines = []
for i in range(m):
    lines.append(list(map(int, input().split())))

def find_ladder_answer(lines):
    grid = [[0] * 15 for _ in range(n)]

    if len(lines) > 0:
        for l in lines:
            r, c = l
            grid[r-1][c-1] = 1
            grid[r][c-1] = -1

    re = []

    for k in range(n):
        dist = 0
        for i in range(15):
            dist = dist + grid[k+dist][i]
        re.append(k+dist)
    
    return re

original_ans = find_ladder_answer(lines)

res = []
ans = m

def recur(count):
    global res, ans

    if count == m:
        if original_ans == find_ladder_answer(res):
            ans = min(ans, len(res))
        return
    
    
    res.append(lines[count])
    recur(count + 1)
    res.pop()
    recur(count + 1)

    

recur(0)

print(ans)



#재귀종료 조건
#사다리를 설치 할 수 없으면 종료
# cnt == 0 and depth == N:
    # return ans

# 사다리 설치
    # a = recur(cnt-1,dept+1)
# 사다리 미설치
    # b = recur(cnt, depth +1)
#    return min(a,b)