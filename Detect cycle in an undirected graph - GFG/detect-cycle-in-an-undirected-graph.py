from typing import List
from collections import defaultdict

class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    
	    def dfs(node,parent):
	        if color[node] == 2:
	            return False
	            
            if color[node] == 1:
               return True
            
            color[node] = 1
            
            for neighbour in adj[node]:
                if parent != neighbour and dfs(neighbour,node):
                   return True
	               
            color[node] = 2
            return False
		
		color = [0]*V
		for node in range(V):
		    if dfs(node,None):
		        return 1
		        
		return 0
		
		    
		


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends