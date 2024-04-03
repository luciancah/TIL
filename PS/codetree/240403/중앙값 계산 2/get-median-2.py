n = int(input())
arr = list(map(int, input().split()))
ans = ''

for i, v in enumerate(arr):
    if (i+1) % 2 == 0:
        continue

    if i == 1:
        ans += arr[i]
        ans += ' '

    
    copy = arr[0:i+1]
    sortedArr = sorted(copy)

    ans += str(sortedArr[i//2])
    ans += ' '

print(ans)