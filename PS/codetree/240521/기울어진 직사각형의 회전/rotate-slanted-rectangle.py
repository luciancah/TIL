n = int(input())
grid = [
    [0] * (n+1) for _ in range(n+1)
]

for i in range(n):
    arr = (list(map(int, input().split())))
    for j in range(n):
        grid[i+1][j+1] = arr[j]

sq = list(map(int, input().split()))
print(sq)

(4, 2), (2, 4), (1, 3), (3, 1)
sq_cor = [[sq[0], sq[1]], [sq[0] - sq[2], sq[1] + sq[2]], [sq[0] - sq[2] - sq[3], sq[1] + sq[2]- sq[3]]], 
            [sq[0] - sq[2] - sq[3] + sq[4], sq[1] + sq[2]- sq[3] - sq[4]]

print(sq_cor)

# def rotate_cw(c0x, c0y, c1x, c1y, c2x, c2y, c3x, c3y):
#     temp = grid[c0x][c0y]

#     for ur in range(c0x, c1y)




# # 직사각형의 경계에 있는 숫자들을 시계 방향으로 한 칸씩 회전해줍니다.
# def rotate(start_row, start_col, end_row, end_col):
#     # Step1-1. 직사각형 가장 왼쪽 위 모서리 값을 temp에 저장합니다.
#     temp = a[start_row][start_col]
    
#     # Step1-2. 직사각형 가장 왼쪽 열을 위로 한 칸씩 shift 합니다.
#     for row in range(start_row, end_row):
#         a[row][start_col] = a[row + 1][start_col]
    
#     # Step1-3. 직사각형 가장 아래 행을 왼쪽으로 한 칸씩 shift 합니다.
#     for col in range(start_col, end_col):
#         a[end_row][col] = a[end_row][col + 1]
    
#     # Step1-4. 직사각형 가장 오른쪽 열을 아래로 한 칸씩 shift 합니다.
#     for row in range(end_row, start_row, -1):
#         a[row][end_col] = a[row - 1][end_col]
    
#     # Step1-5. 직사각형 가장 위 행을 오른쪽으로 한 칸씩 shift 합니다.
#     for col in range(end_col, start_col, -1):
#         a[start_row][col] = a[start_row][col - 1]
    
#     # Step1-6. temp를 가장 왼쪽 위 모서리를 기준으로 바로 오른쪽 칸에 넣습니다.
#     a[start_row][start_col + 1] = temp