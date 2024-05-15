n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def max_diagonal_rectangle_sum(n, grid):
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n

    max_sum = 0

    # 모든 시작점 (i, j) 탐색
    for i in range(n):
        for j in range(n):
            # 길이를 늘려가며 기울어진 직사각형 탐색
            for l1 in range(1, n):
                x1, y1 = i + l1, j + l1
                if not is_valid(x1, y1):
                    break
                
                for l2 in range(1, n):
                    x2, y2 = x1 + l2, y1 - l2
                    if not is_valid(x2, y2):
                        break
                    
                    for l3 in range(1, n):
                        x3, y3 = x2 - l3, y2 - l3
                        if not is_valid(x3, y3):
                            break
                        
                        x4, y4 = x3 - l1, y3 + l1
                        if not is_valid(x4, y4):
                            continue
                        
                        if (x4, y4) == (i, j):
                            # 기울어진 직사각형의 합 계산
                            curr_sum = 0
                            # ↘
                            for k in range(l1):
                                curr_sum += grid[i + k][j + k]
                            # ↙
                            for k in range(l2):
                                curr_sum += grid[x1 + k][y1 - k]
                            # ↖
                            for k in range(l3):
                                curr_sum += grid[x2 - k][y2 - k]
                            # ↗
                            for k in range(l1):
                                curr_sum += grid[x3 - k][y3 + k]
                            max_sum = max(max_sum, curr_sum)

    return max_sum

print(max_diagonal_rectangle_sum(n, arr))