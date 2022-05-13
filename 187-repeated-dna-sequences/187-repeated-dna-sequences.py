class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = defaultdict(int)
        ans = []
        j = 10
        
        def getMask(seq):
            mask = 0
            
            for i in range(10):
                if seq[i] == 'A':
                    mask |= (1<<i)
            
            for i in range(10,20):
                if seq[i%10] == 'C':
                    mask |= (1<<i)
            
            for i in range(20,30):
                if seq[i%10] == 'T':
                    mask  |= (1<<i)
            
            for i in range(30,40):
                if seq[i%10] == 'G':
                    mask |= (1<<i)
                    
            #print(mask)
            return mask

        for i in range(len(s)-9):
            if j <= len(s):
                temp = s[i:i+j]
                mask = getMask(temp)
                
                if seen[mask] == 1:
                    ans.append(temp)
                
                seen[mask] += 1
            
        return ans
                