class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degree = [0]*n
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1
            
        count = [0]*n
        
        queue = deque()
        
        for i in range(n):
            if degree[i] == 1:
                queue.append((i,0))
        
        while queue:
            size = len(queue)
            
            for _ in range(size):
                curr,dist = queue.popleft()
                
                for node in graph[curr]:
                    degree[node] -= 1
                    degree[curr] -= 1
                    
                    if degree[node] > 0:
                        count[node] = max(count[node],1+dist)
                    
                    if degree[node] == 1:
                        queue.append((node,count[node]+1))
                        
        height = max(count)
        
        ans = []
        
        for j in range(n):
            if count[j] == height:
                ans.append(j)
                
        return ans
        