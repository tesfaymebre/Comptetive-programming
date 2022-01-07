class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        diff = []
        for i in range(len(dist)):
            diff.append(dist[i]/speed[i])
        diff.sort()
        print(diff)
        for j in range(len(diff)):
            if j >= diff[j]:
                return j
        return len(diff)
