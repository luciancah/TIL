n = int(input())
arr = []
moves = []

for _ in range(n):
    arr.append(int(input()))

for _ in range(2):
    moves.append(list(map(int, input().split())))

for i in range(len(moves)):
    for j in range(len(arr)):
        if moves[i][0]-1 <= j <= moves[i][1]-1:
            arr[j] = -1
    
    temp_arr = []
    for j in range(len(arr)):
        if arr[j] != -1:
            temp_arr.append(arr[j])
        
    arr = temp_arr

print(len(arr))
for i in range(len(arr)):
    print(arr[i])