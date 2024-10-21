class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        ans = 0
        n = len(s)
        
        def dfs(idx, cnt, visited):
            nonlocal ans
            
            if idx == n: 
                ans = max(ans, cnt)
                return  
            
            for j in range(idx, n):    
                if s[idx:j+1] in visited: 
                    continue  
                    
                visited.add(s[idx:j+1])                
                dfs(j+1, cnt+1, visited)             
                visited.remove(s[idx:j+1]) 
                
        dfs(0, 0, set())                           
        return ans
        