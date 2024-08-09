import heapq

n = int(input())
arr = list(map(int, input().split()))

s = 0
ans = 0
heap = []

heapq.heappush(heap, arr[n-1])
s += arr[n-1]

for i in range(n-2, 0, -1):
    heapq.heappush(heap, arr[i])
    s += arr[i]

    m = heap[0]
    avg = (s - m) / (n - i - 1)

    ans = max(ans, avg)

print(f"{ans:.2f}")