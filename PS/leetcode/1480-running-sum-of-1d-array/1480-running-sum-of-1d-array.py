class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # runningSum[i] = runningSum[i-1] + nums[i]
        result = [nums[0]]
        for i in range(1, len(nums)):
            result.append(result[i-1] + nums[i])
    
        return result