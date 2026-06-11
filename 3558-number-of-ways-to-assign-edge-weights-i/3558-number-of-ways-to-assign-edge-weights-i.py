class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            if not graph[node]:
                return 0

            visited.add(node)
            curr_depth = 0
            for nei in graph[node]:
                if nei not in visited:
                    curr_depth = max(curr_depth, 1 + dfs(nei))

            return curr_depth

        max_depth = dfs(1)

        return (2 ** (max_depth - 1)) % (10**9 + 7)


        