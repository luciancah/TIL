class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefixSum = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            prefixSum[i + 1] = prefixSum[i] + arr[i]

        ans = 0
        for i in range(1, len(arr) + 1, 2):
            for j in range(len(arr) - i + 1):
                ans += prefixSum[j + i] - prefixSum[j]

        return ans