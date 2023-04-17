class Solution:
    def dfs(self,vertex,graph,color):
        for neighbour in graph[vertex]:
            if color[neighbour] == -1:
                color[neighbour] = 1 - color[vertex]
                
                if not self.dfs(neighbour,graph,color):
                    return False
            elif color[vertex] == color[neighbour]:
                return False
            
        return True
        
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1]*len(graph)
        
        for vertex in range(len(graph)):
            if color[vertex] == -1:
                color[vertex] = 0
                
                if not self.dfs(vertex,graph,color):
                    return False
            
        return True
        
        