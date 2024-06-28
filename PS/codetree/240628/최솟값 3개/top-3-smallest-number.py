from heapq import heappush, heappop

n = int(input())
nums = list(map(int, input().split()))

heap = []

def mul_smallest_three(nums):
    res = 1
    temp = []
    for _ in range(3):
        temp.append(heappop(heap))
        # print(temp[-1])
        res *= temp[-1]
    
    for i in range(3):
        heappush(heap, temp[i])

    return res





for i in range(len(nums)):
    heappush(heap, nums[i])
    if i >=2:
        print(mul_smallest_three(heap))
    else:
        print(-1)

# print(heap)