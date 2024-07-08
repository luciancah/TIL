n, s = map(int, input().split())
arr = [0]+list(map(int, input().split()))

ans = 99999999
sum_val = 0
j = 0

for i in range(1, n+1):
    while j+1 <= n and sum_val < s:
        sum_val += arr[j+1]
        j += 1

    if sum_val < s:
        break
    
    ans = min(ans, j-i+1)
    sum_val -= arr[i]

print(ans if ans != 99999999 else -1)