from sys import maxsize
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = maxsize
        left = 0
        current_sum = 0

        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                ans = min(ans, right - left + 1)
                current_sum -= nums[left]
                
                left += 1

        return ans if ans != maxsize else 0
