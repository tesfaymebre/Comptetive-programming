class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = defaultdict(int)

        for u,v in edges:
            indegree[v] += 1

        ans = n
        for u in range(n):
            if indegree[u] == 0:
                if ans != n:
                    return -1

                ans = u

        return ans