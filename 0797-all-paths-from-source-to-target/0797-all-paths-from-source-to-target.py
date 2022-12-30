class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node,path):
            if node == len(graph)-1:
                result.append(path)
                
            for child in graph[node]:
                dfs(child,path + [child])
                
            return
        
        result = []
        dfs(0,[0])
        return result