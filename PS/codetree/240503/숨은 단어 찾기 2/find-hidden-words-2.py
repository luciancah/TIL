n, m = list(map(int, input().split()))
arr = []

for _ in range(n):
    arr.append(input())

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

dxs, dys = [1, 1, 1, -1, -1, -1, 0, 0], [-1, 0, 1, -1, 0, 1, -1, 1]

cnt = 0
for i in range(n):
	for j in range(m):
		
		if arr[i][j] != 'L':
			continue
		
		for dx, dy in zip(dxs, dys):
			curt = 1
			curx = i
			cury = j
			while True:
				nx = curx + dx
				ny = cury + dy
				if in_range(nx, ny) == False:
					break
				if arr[nx][ny] != 'E':
					break
				curt += 1
				curx = nx
				cury = ny
			
			if curt >= 3:
				cnt += 1

print(cnt)