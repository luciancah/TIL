n = int(input())
visited = [False] * (n + 1)
answer = []

def choose(curr_num):
    if curr_num == n+1:
        print(*answer)
        return
    for i in range(n, 0, -1):
        if visited[i]:
            continue

        visited[i] = True
        answer.append(i)

        choose(curr_num + 1)
        answer.pop()
        visited[i] = False

choose(1)