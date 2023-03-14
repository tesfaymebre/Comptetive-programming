class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        def backT(idx,partition):
            if idx == len(num):
                if len(partition) >= 3:
                    return True
                
                return False
            
            for i in range(idx,len(num)):
                temp = num[idx:i+1]
                number = int(temp)
                
                if len(temp) > 1 and temp[0] == '0':
                    continue
                
                if len(partition) < 2 or sum(partition[-2:]) == number:
                    if backT(i+1,partition + [number]):
                        return True
                    
            return False
        
        return backT(0,[])