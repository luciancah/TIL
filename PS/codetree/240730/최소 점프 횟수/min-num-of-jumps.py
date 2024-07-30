n = int(input())
jumps = [int(x) for x in input().split()]
ans = 11

def try_jump(idx, jump_count):
    # print(idx, jump_count)
    global jumps, ans
    if idx > n - 1:
        return
    if idx == n - 1:
        ans = min(ans, jump_count)
    r = jumps[idx] + 1
    for i in range(1, r):
        try_jump(idx + i, jump_count + 1)

try_jump(0, 0)
if ans == 11:
    print(-1)
else:
    print(ans)