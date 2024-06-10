import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
ans = 0
max_ans = 0

def recur(curr_num, ans, count):
    global max_ans

    if count == m:
        max_ans = max(max_ans, ans)
        return
    
    if curr_num == n:
        return

    recur(curr_num+1, ans, count)
    recur(curr_num+1, ans^arr[curr_num], count+1)

recur(0, 0, 0)

print(max_ans)