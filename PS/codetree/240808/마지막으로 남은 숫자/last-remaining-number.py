import heapq

n = int(input())
arr = list(map(int, input().split()))

heap = []

for e in arr:
    heapq.heappush(heap, -e)

while len(heap) > 1:
    [a, b] = [heapq.heappop(heap) for _ in range(2)]
    # if len(heap) == 0:
    #     break
    if a != b:
        heapq.heappush(heap, -abs(a-b))

print(-heap[0] if len(heap) else '-1')