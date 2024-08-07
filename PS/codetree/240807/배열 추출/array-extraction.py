import heapq

n = int(input())
heap = []

for _ in range(n):
    e = int(input())
    if e == 0:
        if len(heap) == 0:
            print(0)
            continue
        print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -e)