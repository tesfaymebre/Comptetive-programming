class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:


        graph = defaultdict(list)
        visited = set()

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
    
        c = 0

        def dfs(node):

            nonlocal c

            for nei in graph[node]:
                if nei in visited: continue
                visited.add(nei)
                values[node]+=dfs(nei)
            
            if values[node] % k == 0:
                c+=1
            
            return values[node]

        visited.add(0)
        dfs(0)

        return c
                    