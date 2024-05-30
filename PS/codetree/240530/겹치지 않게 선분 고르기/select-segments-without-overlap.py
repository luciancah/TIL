n = int(input())
lines = []
answer = []
ans = 0

for _ in range(n):
    lines.append(list(map(int, input().split())))

def is_crossed(lines):
    # print(lines)
    l = sorted(lines, key = lambda x: x[0])
    # print('sorted', l)
    end = l[0][1]
    for i in range(1, len(l)):
        if l[i][0] <= end:
            return True
        if l[i][1] > end:
            end = l[i][1]
    return False

# print(is_crossed([[1,2],[3,4],[5,6]]))

def combinations(n, k):
    def backtrack(start, path):
        if len(path) == k:
            line_answer = [lines[x] for x in path]
            if not is_crossed(line_answer):
                global ans
                ans = len(path)
            return

        for i in range(start, n):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    global ans
    ans = 0
    backtrack(0, [])
    return ans

for k in range(n, 0, -1):
    combinations(n, k)
    if ans != 0:
        print(ans)
        break