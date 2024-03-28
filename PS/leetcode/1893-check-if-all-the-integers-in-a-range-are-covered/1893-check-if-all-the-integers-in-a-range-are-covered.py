class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        new_ranges = []
        target = []
        answer = True
        for r in ranges:
            new_ranges.extend([x for x in range(r[0], r[1] + 1)])
        new_ranges = set(new_ranges)
        for i in range(right-left+1):
            if (i + left) not in new_ranges:
                answer = False
        
        return answer