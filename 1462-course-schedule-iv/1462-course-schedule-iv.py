class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        #using topological sort
        graph = defaultdict(list)
        indegree = defaultdict(int)
        parent = defaultdict(set)
        
        for pre,post in prerequisites:
            graph[pre].append(post)
            parent[post].add(pre)
            indegree[post] += 1
            
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
                
        while queue:
            pre = queue.popleft()

            for post in graph[pre]:
                parent[post].update(parent[pre])
                indegree[post] -= 1

                if indegree[post] == 0:
                    queue.append(post)
       
        return [u in parent[v] for u,v in queries]
                    
        
        """
        #using floyd warshall algorithm
        dp = [[False]*numCourses for _ in range(numCourses)]
        
        for pre,post in prerequisites:
            dp[pre][post] = True
            
        for k in range(numCourses):
            for j in range(numCourses):
                for i in range(numCourses):
                    # if i == k or j == k:
                    #     continue
                    
                    dp[j][i] = dp[j][i] or (dp[j][k] and dp[k][i])
                    
        return [dp[u][v] for u,v in queries]
        """