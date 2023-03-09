class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def backT(i,path):
            if len(path) == k:
                ans.append(path[:])
                return
            
            if i == n+1:
                return
            
            backT(i+1,path + [i])
            backT(i+1,path)
            return
        
        backT(1,[])
        return ans
            