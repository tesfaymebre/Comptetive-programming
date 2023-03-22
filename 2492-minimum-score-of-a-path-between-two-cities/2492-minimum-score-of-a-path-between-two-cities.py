class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for a,b,dis in roads:
            graph[a].append((b,dis))
            graph[b].append((a,dis))
            
        min_score = float('inf')
        
        queue = deque()
        visited= set()
        queue.append(1)
        
        while queue:
            a = queue.popleft()
            visited.add(a)
                
            for b,dis in graph[a]:
                if b not in visited:
                    queue.append(b)
                    min_score = min(min_score,dis)
                    
        return min_score
                    
        
        
