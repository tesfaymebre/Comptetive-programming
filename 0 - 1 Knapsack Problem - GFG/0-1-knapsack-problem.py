#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        #bottom up dp solution
        dp = [[0]*(W+1) for _ in range(n+1)]
        
        for idx in range(n-1,-1,-1):
            for capacity in range(W+1):
                pick = 0
                if wt[idx] <= capacity:
                    pick = val[idx] + dp[idx+1][capacity-wt[idx]]
                
                not_pick = dp[idx+1][capacity]
                
                dp[idx][capacity] = max(pick,not_pick)
                
        return dp[0][W]
            
        
        
        """
        # top down dp solution
        memo = {}
       
        def dp(curr_idx,capacity):
            if curr_idx >= n or capacity <= 0:
                return 0
            
            if (curr_idx,capacity) in memo:
                return memo[(curr_idx,capacity)]
                
            pick = 0
            
            if wt[curr_idx] <= capacity:
                pick = val[curr_idx] + dp(curr_idx+1,capacity-wt[curr_idx])
                
            not_pick = dp(curr_idx+1,capacity)
            
            memo[(curr_idx,capacity)] = max(pick,not_pick)
            return memo[(curr_idx,capacity)]
            
        return dp(0,W)
        """
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends