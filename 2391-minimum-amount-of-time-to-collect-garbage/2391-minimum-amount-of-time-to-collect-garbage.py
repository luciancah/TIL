class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        prefixSum = [0] * (len(travel) + 1)
        for i in range(len(travel)):
            prefixSum[i + 1] = prefixSum[i] + travel[i]
            
        M_idx, G_idx, P_idx = 0, 0, 0
        res = 0
        for i in range(len(garbage)):
            res += len(garbage[i])
            if "M" in garbage[i]:
                M_idx = i
            if "G" in garbage[i]:
                G_idx = i
            if "P" in garbage[i]:
                P_idx = i
        res += prefixSum[M_idx]
        res += prefixSum[G_idx]
        res += prefixSum[P_idx]
            
        return res