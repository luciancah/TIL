class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        ans = []
        for num in nums:
            li = [x for x in range(num[0], num[1] + 1)]
            ans.extend(li)
        ans = set(ans)
        return len(ans)
