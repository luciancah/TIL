n = int(input())
answer = []
a2 = []

def is_beautiful(arr):
    i = 0
    while i < n:
        if i + arr[i] - 1 >= n:
            return False
        for j in range(i, i + arr[i]):
            if arr[j] != arr[i]:
                return False
            
        i += arr[i]
        
    return True

def choose(curr_num):
    if curr_num == n + 1:
        if is_beautiful(answer):
            if is_beautiful(answer):
                a2.append(answer[:])
        return

    for i in range(1, 5):
        answer.append(i)
        choose(curr_num + 1)
        answer.pop()

    return

choose(1)

print(len(a2))