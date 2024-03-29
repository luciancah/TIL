class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = [0]
        for i in range(len(nums)):
            prefixSum.append(prefixSum[i] + nums[i])

        for i in range(len(nums)):
            left = prefixSum[i+1] - prefixSum[0]
            right = prefixSum[-1] - prefixSum[i]
            print(i, left, right)
            if left == right:
                return i
        
        return -1