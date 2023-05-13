from typing import List


from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        graph = defaultdict(list)
        indegree = [0]*(n+1)
        
        for u,v in edges:
            graph[u].append(v)
            indegree[v] += 1
            
        queue = deque()
        
        for i in range(1,n+1):
            if indegree[i] == 0:
                queue.append(i)
                
        time = ['0']*n
        level = 1
    
        while queue:
            size = len(queue)
           
            for _ in range(size):
                curr = queue.popleft()
                time[curr-1] = str(level)
                
                for neighbour in graph[curr]:
                    indegree[neighbour] -= 1
                    
                    if indegree[neighbour] == 0:
                        queue.append(neighbour)
                        
            level += 1
            
        return ' '.join(time)
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        print(res)
        

# } Driver Code Ends