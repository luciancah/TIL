n = int(input())
k = int(input())

'''
arr[i][j] = i*j
1차원으로 flatten 하고 sort 했을때, k번째

답을 가정해서 m보다 같거나 작은 수의 개수를 세어 K 이상이 되는 경우 최솟값
'''

left = 1
right = n*n
ans = right

while left <= right:
    mid = (left + right) // 2

    count = 0
    for i in range(1, n+1):
        count += min(n, mid // i)
    
    if count >= k:
        right = mid - 1
        ans = min(ans, mid)

    else:
        left = mid + 1

print(ans)