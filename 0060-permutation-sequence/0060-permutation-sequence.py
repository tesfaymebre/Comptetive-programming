class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        count = 0
        def backT(seen,path):
            nonlocal count
            
            if len(path) == n:
                count += 1
                
                if count == k:
                    return path[:]
                
                return 
            
            for i in range(1,n+1):
                if i not in seen:
                    seen.add(i)
                    curr = backT(seen,path + [i])
                    
                    if count == k:
                        return curr
                    
                    seen.remove(i)
                    
            return
        
        result = backT(set(),[])
        return "".join([str(num) for num in result ] )