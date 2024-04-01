class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # 두개만 보면 되는구나 ..........
        ans = 0
        edge01 = edges[0] + edges[1]
        for e in edge01:
            if edge01.count(e) == 2:
                return e