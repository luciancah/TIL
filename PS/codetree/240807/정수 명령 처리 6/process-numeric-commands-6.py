import heapq

class PriorityQueue:
    def __init__(self):          # 빈 Priority Queue 하나를 생성합니다.
        self.items = []
                
    def push(self, item):        # 우선순위 큐에 데이터를 추가합니다.
        heapq.heappush(self.items, -item)
                
    def empty(self):             # 우선순위 큐가 비어있으면 True를 반환합니다.
        return not self.items
                
    def size(self):              # 우선순위 큐에 있는 데이터 수를 반환합니다.
        return len(self.items)
        
    def pop(self):               # 우선순위 큐에 있는 데이터 중 최댓값에 해당하는 데이터를 반환하고 제거합니다.
        if self.empty():
            raise Exception("PriorityQueue is empty")
            
        return -heapq.heappop(self.items)
                
    def top(self):               # 우선순위 큐에 있는 데이터 중 최댓값에 해당하는 데이터를 제거하지 않고 반환합니다.
        if self.empty():
            raise Exception("PriorityQueue is empty")
                        
        return -self.items[0]

n = int(input())
pq = PriorityQueue()

for i in range(n):
    opr = list(map(str, input().split()))

    if opr[0] == 'push':
        pq.push(int(opr[1]))
    elif opr[0] == 'size':
        print(pq.size())
    elif opr[0] == 'empty':
        print(1 if pq.empty() else 0)
    elif opr[0] == 'pop':
        print(pq.pop())
    elif opr[0] == 'top':
        print(pq.top())