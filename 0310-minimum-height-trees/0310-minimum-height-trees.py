class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        graph = defaultdict(list)
        degree = [0]*n
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1
        
        queue = deque()
        
        for i in range(n):
            if degree[i] == 1:
                queue.append(i)
        
        count_seen = len(queue)
        
        while queue and count_seen != n:
            size = len(queue)
            
            for _ in range(size):
                curr = queue.popleft()
                
                for neighbour in graph[curr]:
                    degree[neighbour] -= 1
                    degree[curr] -= 1
                    
                    if degree[neighbour] == 1:
                        queue.append(neighbour)
                        
            count_seen += len(queue)
                
        return queue
        