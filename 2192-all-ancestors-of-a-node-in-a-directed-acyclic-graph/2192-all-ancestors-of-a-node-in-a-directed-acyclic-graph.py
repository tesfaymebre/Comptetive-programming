class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indegree = [0] * n
        graph = defaultdict(set)
        ans = [set() for i in range(n)]
        
        for u, v in edges:
            graph[u].add(v)
            ans[v].add(u)
            indegree[v] += 1
            
        queue = deque()
        
        for indx, degree in enumerate(indegree):
            if degree == 0:
                queue.append(indx)
                
        while queue:
            indx = queue.popleft()
            for child in graph[indx]:
                for ancestor in ans[indx]:
                    ans[child].add(ancestor)
                    
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        ans = [sorted(ancestors) for ancestors in ans]
        return ans