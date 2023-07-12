class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        g = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        
        for v, neigbs in enumerate(graph):
            for neigb in neigbs:
                g[neigb].append(v)
                indegree[v] += 1
        
        q = collections.deque()
        
        for v in range(len(graph)):
            if v not in indegree:
                q.append(v)
        
        res = [False] * len(graph)
        while q:
            node = q.popleft()
            
            res[node] = True
            
            for neigb in g[node]:
                indegree[neigb] -= 1
                
                if indegree[neigb] == 0:
                    q.append(neigb)
        
        return [idx for idx in range(len(res)) if res[idx]]
                