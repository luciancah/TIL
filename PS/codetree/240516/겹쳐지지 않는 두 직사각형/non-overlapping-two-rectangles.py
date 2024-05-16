from itertools import combinations

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def calc_sum(x1, y1, x2, y2):
    s = 0
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            s += arr[i][j]
    return s

def rectangles_overlap(a, b):
    # a and b are tuples of (x1, y1, x2, y2)
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b
    # Return true if there is no overlap
    return not (ax2 < bx1 or bx2 < ax1 or ay2 < by1 or by2 < ay1)

# Generate all possible rectangles
all_rectangles = []
for x1 in range(n):
    for y1 in range(m):
        for x2 in range(x1, n):
            for y2 in range(y1, m):
                all_rectangles.append((x1, y1, x2, y2))

max_sum = -float('inf')

# Use combinations to find all pairs of non-overlapping rectangles
for rect1, rect2 in combinations(all_rectangles, 2):
    if not rectangles_overlap(rect1, rect2):
        sum1 = calc_sum(*rect1)
        sum2 = calc_sum(*rect2)
        max_sum = max(max_sum, sum1 + sum2)

print(max_sum)