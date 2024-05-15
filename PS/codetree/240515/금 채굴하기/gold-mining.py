import copy

n, m = list(map(int, input().split()))
arr = []
max_count = 0

for _ in range(n):
    arr.append(list(map(int, input().split())))

k = 0
while k <= 2 * (n-1):
    cb = k*k+(k+1)*(k+1)
    for i in range(n):
        for j in range(n):
            count = 0
            # 마름모 탐색
            for x in range(i-k, i+k+1):
                for y in range(j-k, j+k+1):
                    if abs(x-i) + abs(y-j) > k:
                        continue
                    try:
                        count += arr[x][y]
                    except:
                        continue
                    
                    
                        
            if m * count >= cb:
                max_count = max(count, max_count)
    k+=1


print(max_count)