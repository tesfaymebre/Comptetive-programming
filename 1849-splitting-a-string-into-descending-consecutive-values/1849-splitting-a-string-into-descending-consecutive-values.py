class Solution:
    def splitString(self, s: str) -> bool:
        
        def backT(idx,partition):
            if idx == len(s):
                if len(partition) >= 2:
                    return True
                
                return False
            
            for i in range(idx,len(s)):
                num = int(s[idx:i+1])
                
                if not partition or partition[-1] - 1 == num:
                    if backT(i+1,partition + [num]):
                        return True
                    
            return False
        
        return backT(0,[])