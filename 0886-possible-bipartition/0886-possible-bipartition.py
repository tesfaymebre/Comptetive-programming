class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        def bfs(i):
            queue = deque()
            queue.append(i)
            group[i] = 1
                
            while queue:
                node = queue.popleft()
                
                for child in graph[node]:
                    if group[child] == group[node]:
                        return False
                    
                    if group[child] == 0:
                        queue.append(child)
                        
                        if group[node] == 1:
                            group[child] = 2
                        else:
                            group[child] = 1
                        
            return True
            
        graph = defaultdict(list)
        
        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
            
        group = defaultdict(int)
        
        for i in range(1,n+1):
            if group[i] == 0:
                if not bfs(i):
                    return False
                
        return True