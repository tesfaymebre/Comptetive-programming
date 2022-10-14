class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj_list = defaultdict(list)
        in_degree = dict()
        total_t = 0
        
        for i in range(1,n+1):
            in_degree[i] = [0,0]
        
        for pre,course in relations:
            adj_list[pre].append(course)
            in_degree[course][0] += 1
            
        queue = deque()
        
        for i in range(1,n+1):
            if in_degree[i][0] == 0:
                queue.append([i,in_degree[i]])
                
        while queue:
            i,deg = queue.popleft()
            total_t = max(total_t,time[i-1] + deg[1])
            
            for course in adj_list[i]:
                in_degree[course][1] = max(in_degree[course][1],time[i-1] + deg[1])
                in_degree[course][0] -= 1
                
                if in_degree[course][0] == 0:
                    queue.append([course,in_degree[course]])
                    
        return total_t