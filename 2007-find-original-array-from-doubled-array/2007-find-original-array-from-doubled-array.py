class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        p1 = 0
        p2 = 1
        original = []
        used = set()
        
        # while p2 < len(changed) or p1 < len(changed):
        while len(used) < len(changed):
            if p1 in used and p2 < len(changed):
                if p2-p1 == 1:
                    p1 +=1
                    p2 +=1
                else:
                    p1 +=1
            elif p2 <len(changed) and changed[p1]*2 == changed[p2]:
                original.append(changed[p1])
                used.add(p1)
                used.add(p2)
                p1 +=1
                p2 +=1
                
            elif p2 < len(changed) and changed[p1]*2 > changed[p2]:
                p2+=1
            else:
                return []
        return original
            
        
                
        