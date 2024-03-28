class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        prefixSum = [0] * (len(nums) + 1)
        ans = 0
        for i in range(len(nums)):
            prefixSum[i+1] = prefixSum[i] + nums[i]

        for i in range(1, len(prefixSum)):
            if prefixSum[i] == 0:
                ans += 1
        
        return ans
        