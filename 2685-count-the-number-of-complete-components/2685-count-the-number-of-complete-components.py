class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for p, c in edges:
            graph[p].append(c)
            graph[c].append(p)
        visted = set()
        
        def dfs(node):
            
            
            for adj in graph[node]:
                if (adj, node) not in edge:
                    edge.add((node, adj))
                    
                if adj not in visted:
                    visted.add(adj)
                    vertixs.add(adj)
                    
                    dfs(adj)
            
            
        count = 0
        for i in range(n):
            if i not in visted:
                edge = set()
                vertixs = set()
                dfs(i) 
                len_v = len(vertixs)
                if len(edge) >= int((len_v * (len_v-1)/2)):
                    count+=1
                # print(i, edge)
        return count