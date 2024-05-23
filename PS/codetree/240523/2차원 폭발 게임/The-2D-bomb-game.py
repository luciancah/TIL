BLANK = -1
WILL_EXPLODE = 0

# 변수 선언 및 입력
n, m, k = tuple(map(int, input().split()))
numbers_2d = [
    list(map(int, input().split()))
    for _ in range(n)
]
numbers_1d = [
    0 for _ in range(n)
]


# 주어진 시작점에 대하여
# 부분 수열의 끝 위치를 반환합니다.
def get_end_idx_of_explosion(start_idx, curr_num):
    for end_idx in range(start_idx + 1, len(numbers_1d)):
        if numbers_1d[end_idx] != curr_num:
            return end_idx - 1
        
    return len(numbers_1d) - 1


def explode():
    while True:
        did_explode = False
        curr_idx = 0
    
        while curr_idx < len(numbers_1d):
            end_idx = get_end_idx_of_explosion(curr_idx, numbers_1d[curr_idx])
        
            if end_idx - curr_idx + 1 >= m:
                # 연속한 숫자의 개수가 m개 이상이면
                # 폭탄이 터질 수 있는 경우 해당 부분 수열을 잘라내고
                # 폭탄이 터졌음을 기록해줍니다.
                del numbers_1d[curr_idx:end_idx + 1]
                did_explode = True
            else:
                # 주어진 시작 원소에 대하여 폭탄이 터질 수 없는 경우
                # 다음 원소에 대하여 탐색하여 줍니다.
                curr_idx = end_idx + 1

        if not did_explode:
            break


##################################################################################
##			이 줄을 기준으로 위에 있는 함수들에 대한 설명은 1차원 폭발 게임을 참조해주세요     	  ##
##################################################################################

        
# 격자의 특정 열을 일차원 배열에 복사해줍니다.
def copy_column(col):
    global numbers_1d
    
    numbers_1d = [
        numbers_2d[row][col]
        for row in range(n)
        if numbers_2d[row][col] != BLANK
    ]


# 폭탄이 터진 결과를 격자의 해당 열에 복사해줍니다.
def copy_result(col):
    for row in range(n - 1, -1, -1):
        numbers_2d[row][col] = numbers_1d.pop() if numbers_1d \
                                                else BLANK


# 폭탄이 터지는 과정을 시뮬레이션 합니다.
def simulate():
    for col in range(n):
        copy_column(col)
        explode()
        copy_result(col)

        
# 시계 방향으로 90도 회전해줍니다.
def rotate():
    global numbers_2d
    
    # 빈 칸으로 초기화 된 임시 격자를 선언합니다.
    temp_2d = [
        [BLANK for _ in range(n)]
        for _ in range(n)
    ]
    
    # 기존 격자를 시계 방향으로 90도 회전했을 때의 결과를
    # 임시 격자에 저장해줍니다.
    for i in range(n - 1, -1, -1):
        curr_idx = n - 1
        for j in range(n - 1, -1, -1):
            if numbers_2d[i][j] != BLANK:
                temp_2d[curr_idx][n - i - 1] = numbers_2d[i][j]
                curr_idx -= 1
    
    # 임시 격자에 저장된 값을 기존 격자에 복사합니다.
    numbers_2d = temp_2d

        
# 주어진 입력에 따라 폭탄이 터지는 것을 시뮬레이션 합니다.
simulate()
for _ in range(k):
    rotate()
    simulate()

        
# 격자를 순회하며 남아 있는 폭탄의 개수를 세줍니다.
answer = sum([
    numbers_2d[i][j] != BLANK
    for i in range(n)
    for j in range(n)
])
print(answer)