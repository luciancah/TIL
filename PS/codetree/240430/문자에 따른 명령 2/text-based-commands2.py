cmd_lst = input()
dir_num = 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0

for i in range(len(cmd_lst)):
    if cmd_lst[i] == 'L':
        dir_num -= 1
        if dir_num < 0:
            dir_num += 4
    elif cmd_lst[i] == 'R':
        dir_num += 1
        if dir_num > 3:
            dir_num %= 4
    elif cmd_lst[i] == 'F':
        x += dx[dir_num]
        y += dy[dir_num]
print(x, y)