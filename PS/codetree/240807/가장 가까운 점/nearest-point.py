import heapq

n, m = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]

heap = []

for e in arr:
    heapq.heappush(heap, (abs(e[0])+abs(e[1]), e[0], e[1]))

for _ in range(m):
    temp = heapq.heappop(heap)
    tx, ty = temp[1], temp[2]
    heapq.heappush(heap, (tx+ty+4, tx+2, ty+2))

print(' '.join(map(str, heap[0][1:])))