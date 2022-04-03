class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.pairs = defaultdict(list)
        
        for i in range(len(edges)):
            edges[i].sort()
            
        for i in range(len(edges)):
            self.pairs[edges[i][0]].append(edges[i][1])
            self.pairs[edges[i][1]].append(edges[i][0])
            
        self.ans = False
        
        def recur(vertex):
            if vertex == destination:
                self.ans = True
                return
            
            while self.pairs[vertex] and self.ans == False:
                recur(self.pairs[vertex].pop())
                
        recur(source)
        return self.ans
            