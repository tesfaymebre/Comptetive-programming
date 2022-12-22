class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for v1,v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
            
        memo = {}
        visited = [False]*n
        
        def dfs(node):
            visited[node] = True
            node_dist,node_neighbours = 0,0
            
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    nei_dist,nei_neighbours = dfs(neighbour)

                    node_dist  += nei_dist
                    node_neighbours += nei_neighbours
            
            node_dist += node_neighbours
            
            memo[node] = (node_dist,node_neighbours)
            return (node_dist,node_neighbours+1)
        
        dfs(0)
        
        result = [0]*n
        visited = [False]*n
        
        def find(node):
            visited[node] = True
            
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    node_dist,node_neighbours = memo[node]
                    nei_dist,nei_neighbours = memo[neighbour]
                    
                    dist = node_dist - (nei_neighbours+1)
                    dist += n-(nei_neighbours+1)
                    
                    result[neighbour] = dist
                    memo[neighbour] = (dist,node_neighbours)
                    
                    find(neighbour)
        
        find(0)
        result[0] = memo[0][0]
        
        return result
            