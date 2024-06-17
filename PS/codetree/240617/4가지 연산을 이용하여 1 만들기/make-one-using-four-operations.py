from collections import deque

n = int(input())
min_ans = 99999

q = deque()
visited = [0 for _ in range(2*n)]
step = [0 for _ in range(2*n)]

def in_range(num):
    return 1 <= num <= 2*n-1

def can_go(num):
    return in_range(num) and not visited[num]

# def calc(num, operator):
#     if operator == 0:
#         return num - 1
#     if operator == 1:
#         return num + 1
#     if operator == 2:
#         if num % 2 == 0:
#             return num 

def bfs():
    while q:
        curr_num = q.popleft()

        for i in range(4):
            if i == 0:
                new_num = curr_num - 1
            if i == 1:
                new_num = curr_num + 1
            if i == 2:
                if curr_num % 2 == 0:
                    new_num = curr_num // 2
            if i == 3:
                if curr_num % 3 == 0:
                    new_num = curr_num // 3
            
            if can_go(new_num):
                visited[new_num] = 1
                step[new_num] = step[curr_num] + 1
                q.append(new_num)

    return step[1]

visited[n] = 1
step[n] = 1
q.append(n)
print(bfs()-1)