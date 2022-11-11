class Solution:
    def numSquares(self, n: int) -> int:
        #bfs solution
        
        squares = [i*i for i in range(1,floor(sqrt(n))+1)]
        queue = deque([n])
        depth = 1
        
        while queue:
            size_queue = len(queue)
            
            for j in range(size_queue):
                curr = queue.popleft()
                
                for square in squares:
                    if curr == square:
                        return depth
                    if curr < square:
                        break
                        
                    queue.append(curr-square)
                    
            depth += 1
            
        return depth
        
        """
        # bottom up dp solution
        dp = [0] + [float('inf')]*n
        
        for i in range(1,n+1):
            dp[i] = min(dp[i-j*j] for j in range(1,floor(sqrt(i))+1)) + 1
            
        return dp[n]
        """