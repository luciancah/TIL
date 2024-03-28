class Solution:
    def pivotInteger(self, n: int) -> int:
        ans = -1
        leftSum = 0
        rightSum = 0
        nums = [i for i in range(n)]
        allSum = 0
        
        for i in range(1, n + 1):
            allSum += i

        for i in range(1, n + 1):
            leftSum += i
            rightSum = allSum - leftSum
            if leftSum - i == rightSum:
                ans = i
        return ans

