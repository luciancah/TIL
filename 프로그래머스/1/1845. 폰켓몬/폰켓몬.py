from itertools import combinations
from collections import defaultdict

def solution(nums):
    answer = 0
    d = defaultdict(int)
    
    for n in nums:
        d[n] += 1
        
    d = list(d)
        
    answer = len(d) if len(d) <= len(nums) // 2 else len(nums)//2
        
    return answer
