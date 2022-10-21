class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_graph = defaultdict(list)
        row_indegree = [0]*(k+1)
        col_graph = defaultdict(list)
        col_indegree = [0]*(k+1)
        
        for above,below in rowConditions:
            row_graph[above].append(below)
            row_indegree[below] += 1
            
        for left,right in colConditions:
            col_graph[left].append(right)
            col_indegree[right] += 1
            
        queue = deque()
        count = 0
        col_position = dict()
        col = 1
        
        for i in range(1,k+1):
            if col_indegree[i] == 0:
                queue.append(i)
                
        while queue:
            size = len(queue)
            count += size
            
            for i in range(size):
                left = queue.popleft()
                col_position[left] = col
                col += 1
                
                for right in col_graph[left]:
                    col_indegree[right] -= 1
                    if col_indegree[right] == 0:
                        queue.append(right)
                        
        if len(col_graph) != count:
            return []
        
        queue = deque()
        matrix = [[0]*k for _ in range(k)]
        count = 0
        row = 1
        
        for i in range(1,k+1):
            if row_indegree[i] == 0:
                queue.append(i)
                
        while queue:
            size = len(queue)
            count += size
            
            for i in range(size):
                above = queue.popleft()
                
                if above in col_position:
                    matrix[row-1][col_position[above]-1] = above
                else:
                    matrix[row-1][-1] = above
                    
                row += 1
                    
                for below in row_graph[above]:
                    row_indegree[below] -= 1
                    if row_indegree[below] == 0:
                        queue.append(below)
                        
        if count != len(row_graph):
            return []
        
        return matrix
        
        