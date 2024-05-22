n, m = list(map(int, input().split()))
arr = []

for _ in range(n):
    arr.append(int(input()))

def check_bomb(arr, m):
    new_arr = []
    i = 0

    while (i < len(arr)):
        j = i
        while (j < len(arr) - 1 and arr[j] == arr[j+1]):
            j += 1
        if (j - i + 1 >= m):
            i = j + 1
        else:
            new_arr.extend(arr[i:j+1])
            i = j + 1

    return new_arr

        
while True:
    new_arr = check_bomb(arr, m)
    if len(new_arr) == len(arr):
        break
    arr = new_arr

if len(new_arr) == 0:
    print(0)
else:
    print(len(new_arr))
    for i in range(len(new_arr)):
        print(new_arr[i])