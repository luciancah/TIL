import sys

n, m = list(map(int, input().split()))
dots = []
for _ in range(n):
    dots.append(list(map(int, input().split())))

def calc_dist(a, b):
    res = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
    return res

# 재귀 1사이클 : m개 될때까지 고를까 말까 / 안에서 가장 먼 두점 거리 구하기

min_dist = sys.maxsize
selected_dots = []

def recur(count, curr_index, selected_dots):
    global min_dist
    max_dist = 0
    if count == m:
        for i in range(len(selected_dots)):
            for j in range(i+1, len(selected_dots)):
                dist = calc_dist(selected_dots[i], selected_dots[j])
                max_dist = max(dist, max_dist)
        min_dist = min(min_dist, max_dist)
        return

    if curr_index == n:
        return

    # 얘 고를지 말지
    selected_dots.append(dots[curr_index])
    recur(count+1, curr_index+1, selected_dots)
    selected_dots.pop()
    recur(count, curr_index+1, selected_dots)

recur(0, 0, selected_dots)

print(min_dist)