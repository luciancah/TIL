import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))

heap = []
for e in arr:
    heapq.heappush(heap, -e)

for i in range(m):
    temp = heapq.heappop(heap)
    temp += 1
    heapq.heappush(heap, temp)

print(-heap[0])