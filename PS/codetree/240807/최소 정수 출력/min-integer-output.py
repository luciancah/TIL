import heapq

n = int(input())
heap = []

for _ in range(n):
    e = int(input())
    if e == 0:
        if len(heap) == 0:
            print(0)
            continue
        sm = heapq.heappop(heap)
        print(sm)
    else:
        heapq.heappush(heap, e)