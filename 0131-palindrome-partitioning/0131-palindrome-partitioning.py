class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def helper(left,path):
            if left == len(s):
                self.result.append(path)
                return
            
            for right in range(left,len(s)):
                if s[left:right+1] == s[left:right+1][::-1]:
                    helper(right+1,path + [s[left:right+1]])
                    
            return
        
        self.result = []
        
        helper(0,[])
        
        return self.result