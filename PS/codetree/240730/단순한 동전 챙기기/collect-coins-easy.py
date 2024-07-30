# 최소 3개의 동전 수집
# 번호가 증가하는 순서대로 수집
# 동전 위를 지나가도 수집하지 않아도 됨
# 같은 위치 2번 이상 지나도 됨
n = int(input())
mat = []
coin_locations = {}
s_row, s_col = 0, 0
e_row, e_col = 0, 0
ans = float("inf")
for k in range(n):
    buf = list(input())
    for i in range(len(buf)):
        if buf[i] == 'S':
            s_row, s_col = k, i
        if buf[i] == 'E':
            e_row, e_col = k, i
        if buf[i] != '.' and buf[i] != 'S' and buf[i] != 'E':
            buf[i] = int(buf[i])
            coin_locations[buf[i] - 1] = [k, i]
    mat.append(buf)
coins = list(coin_locations.keys())
if len(coins) < 3:
    print(-1)
    exit()
coins.sort()

def travel(row, col, dest_row, dest_col, move_cnt):
    if row < dest_row:
        while row < dest_row:
            row += 1
            move_cnt += 1
    elif row > dest_row:
        while row > dest_row:
            row -= 1
            move_cnt += 1
    if col < dest_col:
        while col < dest_col:
            col += 1
            move_cnt += 1
    elif col > dest_col:
        while col > dest_col:
            col -= 1
            move_cnt += 1
    return move_cnt

# 등장한 숫자 중 3개의 순열(오름차순)을 모두 뽑아 백트레킹한다.
# 멈추는 지점은 동전 위 뿐이다.
def try_path(coin_cnt, move_cnt, idx):
    # print(coin_cnt, move_cnt, idx)
    global coins, coin_locations, ans
    if coin_cnt >= 3:
        move_cnt = travel(coin_locations[coins[idx]][0], coin_locations[coins[idx]][1], e_row, e_col, move_cnt)
        ans = min(ans, move_cnt)
        return
    coin_len = len(coins)
    for i in range(idx + 1, coin_len):
        new_move_cnt = travel(coin_locations[coins[idx]][0], coin_locations[coins[idx]][1],
        coin_locations[coins[i]][0], coin_locations[coins[i]][1], move_cnt)
        try_path(coin_cnt + 1, new_move_cnt, i)
for i in range(len(coins)):
    try_path(1, travel(s_row, s_col, coin_locations[coins[i]][0], coin_locations[coins[i]][1], 0), i)
print(ans)