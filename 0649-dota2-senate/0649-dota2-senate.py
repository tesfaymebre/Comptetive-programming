class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        occurence = Counter(list(senate))
        visited = set()
        ptr1 = 0
        
        while occurence['R'] > 0 and occurence['D'] > 0:
            if ptr1 == len(senate):
                ptr1 = 0
         
            find = 'D' if senate[ptr1] == 'R' else 'R'
            ptr2 = ptr1 + 1
            
            while ptr1 not in visited:
                if ptr2 == len(senate):
                    ptr2 = 0
                
                if ptr2 not in visited and senate[ptr2] == find:
                    occurence[find] -= 1
                    visited.add(ptr2)
                    break
                ptr2 += 1
                    
            ptr1 += 1
            
        return "Radiant" if occurence['R'] > 0 else "Dire" 
