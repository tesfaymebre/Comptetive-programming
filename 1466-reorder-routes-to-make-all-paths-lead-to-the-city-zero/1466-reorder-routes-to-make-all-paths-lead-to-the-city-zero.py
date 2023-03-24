class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for a,b in connections:
            graph[a].append((b,1))
            graph[b].append((a,-1))
            
        queue = deque()
        visited = set()
        
        queue.append(0)
        visited.add(0)
        
        edge_changes = 0
        
        while queue:
            size = len(queue)
            
            for i in range(size):
                city = queue.popleft()
                visited.add(city)
                
                for connected_city,direction in graph[city]:
                    if connected_city not in visited:
                        if direction == 1:
                            edge_changes += 1

                        queue.append(connected_city)
                        
        return edge_changes