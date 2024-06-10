n = int(input())
arr = list(map(int, input().split()))

'''
현재 위치에서 쓰여진 숫자만큼 돌면서 recur 태우고
밖으로 나가면 나가서 횟수 세기
'''
min_count = 99999

def recur(pos, count):
    # print(pos, count)
    global min_count
    if pos >= n-1:
        min_count = min(count, min_count)
        return
    elif count == 5:
        return

    for i in range(arr[pos], 0, -1):
        recur(pos + i, count + 1)

recur(0, 0)

if min_count == 99999:
    print(-1)
else:
    print(min_count)