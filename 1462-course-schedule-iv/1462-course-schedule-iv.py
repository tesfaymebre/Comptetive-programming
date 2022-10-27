class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dp = [[False]*numCourses for _ in range(numCourses)]
        
        for pre,post in prerequisites:
            dp[pre][post] = True
            
        for k in range(numCourses):
            for j in range(numCourses):
                for i in range(numCourses):
                    if i == k or j == k:
                        continue
                    
                    dp[j][i] = dp[j][i] or (dp[j][k] and dp[k][i])
                    
        return [dp[u][v] for u,v in queries]