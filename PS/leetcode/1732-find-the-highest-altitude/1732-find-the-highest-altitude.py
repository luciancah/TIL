class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefixSum = [0] * (len(gain) + 1)
        for i in range(len(gain)):
            prefixSum[i + 1] = prefixSum[i] + gain[i]
        prefixSum.sort()
        return prefixSum[-1]
        