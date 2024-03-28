class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = [0]
        rightSum = [0]
        result = []
        for i in range(0, len(nums)):
            leftSum.append(leftSum[i] + nums[i])
        nums.reverse()
        for i in range(0, len(nums)):
            rightSum.append(rightSum[i] + nums[i])

        leftSum = leftSum[:-1]
        rightSum = rightSum[:-1]
        rightSum.reverse()

        for i in range(0, len(leftSum)):
            result.append(abs(leftSum[i] - rightSum[i]))

        return result