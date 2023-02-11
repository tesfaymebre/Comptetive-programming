class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        visited = set()
        que = deque()
        ans = [-1]*n
        
        for st,ed in redEdges:
            adj_list[st].append((ed,'r'))
        
        for st,ed in blueEdges:
            adj_list[st].append((ed,'b'))
            
        que.append((0,'unknown',0))
        
        while que:
            st,color,level = que.popleft()
            
            if ans[st] == -1:
                ans[st] = level
            
            for end in adj_list[st]:
                if (st,end[0],end[1]) not in visited and color != end[1]:
                    que.append((end[0],end[1],level+1))
                    visited.add((st,end[0],end[1]))
                    
        return ans
        