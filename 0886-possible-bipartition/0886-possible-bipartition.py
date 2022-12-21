class UnionFind:
    def __init__(self,size):
        self.parent = [i for i in range(size)]
        self.rank = [0]*size
        
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            
        return self.parent[x]
    
    def union(self,x,y):
        par_x = self.find(x)
        par_y = self.find(y)
        
        if par_x == par_y:
            return
        
        if self.rank[par_x]  < self.rank[par_y]:
            par_x,par_y = par_y,par_x
            
        self.parent[par_y] = par_x
        self.rank[par_x] += self.rank[par_y]
        return
    
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
            
        DSU = UnionFind(n+1)
        
        for node in range(1,n+1):
            for child in graph[node]:
                if  DSU.find(node) == DSU.find(child):
                    return False
                
                DSU.union(graph[node][0],child)
        
        return True
        
        """
        #bfs approach
        
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
        """